# import graund
import sqlite3
from pathlib import Path
# connect sqlite database
database_path = Path(__file__).parent / "tasks.db"
database_path_string = str(database_path.absolute())
conn = sqlite3.connect(database_path_string)
# create cursor
c = conn.cursor()
# create table structure if doesn't exist
c.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        created_date TEXT NOT NULL,
        tags TEXT,
        completed INTEGER DEFAULT 0
    )
""")
# commit structure to database
conn.commit()


def add_task_db(title, created_date, tags):
    """
    add task to database
    """
    c.execute(
        """
        INSERT INTO tasks
            (title, created_date, tags)
        VALUES (?, ?, ?)
        """,
        (title, created_date, tags),
    )

    conn.commit()
    print("Task added.")


def log_tasks_db():
    """
    ask database fo this information from task table
    """
    c.execute("""
    SELECT id, title, created_date, tags, completed
    FROM tasks
    ORDER BY completed, created_date DESC
    """)

    # fetches all cases from database
    rows = c.fetchall()

    return rows


def complete_task_db(choice):
    """
    change completation state in
    """
    c.execute(
        """
              UPDATE tasks
              SET completed = NOT completed
              WHERE id = ?
              """,
        (choice,),
    )
    conn.commit()


def delete_task_db(task_id):
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    conn.commit()


def search_by_tag_db(tag):
    c.execute(
        """
        SELECT *
        FROM tasks
        WHERE tags LIKE ?
        """,
        (f"%{tag}%",),
    )

    return c.fetchall()
