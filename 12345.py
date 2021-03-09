from tkinter import *
from tkinter import messagebox
import pickle
root = Tk()
root.geometry("300x500")
root.title('Войти в систему')
root["bg"]="#F2E9E4"

def registration():
    text = Label(text="Для входа в систему - зарегистрируйтесь!", font=("Times New Roman", 12), background="#9A8C98", foreground="#22223B")
    text_login = Label(text="Введите логин: ", font=("Times New Roman", 16),  foreground="#22223B")
    registr_login = Entry(bd=1, font="Arial 12", foreground="#22223B", background="#C9ADA7")
    text_password1 = Label(text="Введите пароль: ", font=("Times New Roman", 16),  foreground="#22223B")
    registr_password1 = Entry(bd=1, font="Arial 12", foreground="#22223B", background="#C9ADA7")

    text_password2 = Label(text="Повторите пароль: ", font=("Times New Roman", 16),  foreground="#22223B")
    registr_password2 = Entry(show="*",bd=1, font="Arial 12", foreground="#22223B", background="#C9ADA7" )
    button_registr = Button(text="Зарегистрироваться", background="#9A8C98", foreground="#22223B", font=("Arial", 12, "bold"), border=2, command=lambda: save())
    text.pack()
    text_login.pack()
    registr_login.pack()
    text_password1.pack()
    registr_password1.pack()
    text_password2.pack()
    registr_password2.pack()
    button_registr.pack()

    def save():
        login_pass_save = {}
        login_pass_save[registr_login.get()] = registr_password1.get()
        f = open('login_pass.txt', 'wb')
        pickle.dump(login_pass_save, f)
        f.close()
        login()


def login():
    text_log = Label(text="Теперь Вы можете войти в систему.", font=("Times New Roman", 12), background="#9A8C98", foreground="#22223B")
    text_enter_login = Label(text="Введите логин: ", font=("Times New Roman", 16), background="#9A8C98", foreground="#22223B")
    enter_login = Entry(show="*", bd=1, font="Arial 12", foreground="#22223B", background="#C9ADA7")
    text_enter_pass = Label(text="Введите пароль: ",font=("Times New Roman", 16), background="#9A8C98", foreground="#22223B")
    enter_password = Entry(show="*", bd=1, font="Arial 12", foreground="#22223B", background="#C9ADA7")
    text_log.pack()
    button_login = Button(text="Войти",  background="#9A8C98", foreground="#22223B", font=("Arial", 12, "bold"), border=2, command=lambda: log_pass())
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_password.pack()
    button_login.pack()

    def log_pass():
        f = open('login_pass.txt', 'rb')
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() == a[enter_login.get()]:
                messagebox.showinfo("Вход выполнен!","Ирина Сергеевна, поставьте, пожалуйста 5!<3")
            else:
                messagebox.showerror("Ошибка!", "Неверный пароль.")
        else:
            messagebox.showerror("Ошибка!", "Неверный логин.")


registration()
root.mainloop()