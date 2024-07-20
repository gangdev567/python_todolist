from db_connector import get_connection

todo_list = []
users = {
  "users1": "password1",
  "user2": "password2"
}

def login(username, password):
  """사용자 로그인 함수"""
  if username in users and users[username] == password:
    print(f"{username}님 환영합니다")
    return True
  else:
    print("로그인 실패")
    return False
  
def save_todo(username, todo_item):
  """새로운 To-Do 항목을 저장하는 함수"""
  db = get_connection()
  cursor = db.cursor()
  
  query = "INSERT INTO todolist_db (username, item) VALUES (%s, %s)"
  cursor.execute(query, (username, todo_item))
  
  db.commit()
  print("Todo List 항목이 저장되었습니다.")
  
  cursor.close()
  db.close()

def add_todo(username):
  """새로운 To-Do 항목을 추가하는 함수"""
  todo_item = input("To-Do List 항목을 입력하세요: ")
  save_todo(username, todo_item)
  
def view_todos(username):
  """현재 모든 To-Do 항목을 보여주는 함수"""
  db = get_connection()
  cursor = db.cursor()
  
  query = "SELECT item FROM todolist_db WHERE username = %s"
  cursor.execute(query, (username,))
  
  todos = cursor.fetchall()
  
  if todos:
    print("\n현재 To-Do 목록:")
    for i, todo in enumerate(todos, start=1):
      print(f"{i}. {todo}")
  else:
    print(f"\n현재 {username}의 To-Do 목록이 비어 있습니다.")

def delete_todo():
  """특정 To-Do 항목을 삭제하는 함수"""
  db = get_connection()
  cursor = db.cursor()
  
  try:
    index = int(input("삭제할 항목의 번호를 입력하세요: ")) -1
    if 0 <= index < len(todo_list):
      deleted_todo = todo_list.pop(index)
      print(f"'{deleted_todo}'가 목록에서 삭제되었습니다.")
    else:
      print("유효하지 않은 번호입니다.")
  except ValueError:
      print("숫자를 입력해주세요.")

def exit_program():
  """프로그램을 종료하는 함수"""
  db = get_connection()
  cursor = db.cursor()
  
  print("\nTo-Do List 애플리케이션을 종료합니다.")
  exit()

def main():
  print("\n=== 로그인 하십시오 ===")
  username = input("아이디: ")
  password = input("비밀번호: ")
  login(username, password)
  
  """메인 루프"""
  while True:
    print("\n=== To-Do List ===")
    print("1. 새 항목 추가")
    print("2. 현재 목록 보기")
    print("3. 항목 삭제")
    print("4. 프로그램 종료")
    
    try:
      choice = int(input("선택하세요: "))
      
      if choice == 1:
        add_todo(username)
      elif choice == 2:
        view_todos(username)
      elif choice == 3:
        delete_todo(username)
      elif choice == 4:
        exit_program()
      else:
        print("잘못된 선택입니다.")
    except ValueError:
      print("숫자를 입력하세요")

if __name__ == "__main__":
  main()