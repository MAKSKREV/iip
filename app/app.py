import streamlit as st
import random
import time
import sqlite3
import os

# Проверяем, существует ли база данных, и создаем её, если нет
db_file = 'database.db'
if not os.path.exists(db_file):
    open(db_file, 'w').close()  # Создаем пустой файл базы данных

# Подключение к базе данных SQLite
conn = sqlite3.connect(db_file)

# Функция для создания таблиц, если они не существуют
def create_tables():
    with conn:
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                balance INTEGER NOT NULL DEFAULT 50
            )
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                item_name TEXT,
                item_value INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
create_tables()

# Функция для получения или создания пользователя
def get_or_create_user(user_id, first_name):
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,))
        result = cur.fetchone()
        
        if result is None:
            # Если пользователь не найден, создаем его
            cur.execute("INSERT INTO users (user_id, first_name) VALUES (?, ?)", (user_id, first_name))
            return 50  # Начальный баланс
        else:
            return result[0]  # Возвращаем текущий баланс

# Функция для обновления баланса пользователя
def update_user_balance(user_id, new_balance):
    with conn:
        cur = conn.cursor()
        cur.execute("UPDATE users SET balance = ? WHERE user_id = ?", (new_balance, user_id))

# Функция для сохранения выбитого предмета
def save_item(user_id, item_name, item_value):
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO items (user_id, item_name, item_value) VALUES (?, ?, ?)", (user_id, item_name, item_value))

# Функция для получения всех выбитых предметов пользователя
def get_user_items(user_id):
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT item_name, item_value FROM items WHERE user_id = ?", (user_id,))
        return cur.fetchall()

# Элементы для игры с шансами
items_with_chances = {
    'image0.webp': (0, 0.5),  # 50% шанс
    'image1.png': (5, 0.2),   # 20% шанс
    'image2.jpg': (15, 0.1),  # 10% шанс
    'image3.webp': (1, 0.008),   # 0,8% шанс
    'image4.webp': (7, 0.005),  # 0,5% шанс
    'image5.webp': (30, 0.001)   # 0,1% шанс
}

def spin_items():
    spin_duration = 3  
    end_time = time.time() + spin_duration
    selected_item = None

    while time.time() < end_time:
        selected_item = random.choices(
            list(items_with_chances.keys()),
            weights=[chance for _, chance in items_with_chances.values()],
            k=1
        )[0]
        time.sleep(0.5)  
    return selected_item

# Навигация по страницам
st.sidebar.title("Навигация")
page = st.sidebar.radio("Выберите страницу:", ["Крутилка", "Профиль"])

# Получаем user_id и first_name из session_state
user_id = st.session_state.get('user_id', None)
first_name = st.session_state.get('first_name', None)

if user_id is not None and first_name is not None:
    # Получаем или создаем пользователя
    balance = get_or_create_user(user_id, first_name)
    st.session_state.balance = balance  # Сохраняем баланс в session_state
else:
    st.error("Пожалуйста, войдите через бота.")

# Страница крутилки
if page == "Крутилка":
    st.title("Крутилка")
    
    if 'balance' in st.session_state:
        st.write(f"Добро пожаловать, {first_name}! Ваш баланс: {st.session_state.balance} звёзд.")
        
        # Проверка, достаточно ли средств для крутки
        if st.session_state.balance >= 25:
            if 'spin_button_clicked' not in st.session_state:
                st.session_state.spin_button_clicked = False

            if st.session_state.spin_button_clicked:
                st.button("Крутить!", disabled=True)  # Кнопка отключена после нажатия
                with st.spinner("Раскручиваем барабан..."):
                    selected_item = spin_items()
                    st.image(selected_item, width=200)
                    item_value = items_with_chances[selected_item][0]
                    st.write(f"Вы получили {item_value} звёзд")
                    
                    # Сохраняем выбитый предмет
                    save_item(user_id, selected_item, item_value)

                    # Обновляем баланс
                    new_balance = st.session_state.balance - 25
                    st.session_state.balance = new_balance
                    update_user_balance(user_id, new_balance)  # Обновляем баланс в базе данных

                st.session_state.spin_button_clicked = False  # Сбрасываем состояние кнопки после выполнения
            else:
                if st.button("Крутить!"):
                    st.session_state.spin_button_clicked = True  # Устанавливаем состояние кнопки при нажатии
        else:
            st.error("Недостаточно средств для крутки. Вам нужно минимум 25 рублей на балансе.")
    else:
        st.error("Пожалуйста, войдите, чтобы играть.")

# Страница профиля
elif page == "Профиль":
    st.title("Профиль")
    
    if 'balance' in st.session_state:
        st.write(f"Добро пожаловать в ваш профиль, {first_name}!")
        st.write(f"Ваш баланс: {st.session_state.balance} звёзд.")
        
        items_list = get_user_items(user_id)
        
        if items_list:
            st.subheader("Выбитые предметы:")
            for item_name, item_value in items_list:
                st.write(f"{item_value} звёзд")
                st.image(item_name, width=100)  
        else:
            st.write("Вы пока ничего не выбили.")
    else:
        st.error("Пожалуйста, войдите, чтобы просмотреть свой профиль.")