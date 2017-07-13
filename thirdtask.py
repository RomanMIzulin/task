# Написать программу, которая:
# выполняет запуск приложения под Windows, 
# печатает в консоль текст заголовка главного окна запущенного приложения, 
# закрывает запущенное приложение и 
# выполняет проверку успешности закрытия ранее запущенного приложения.

# Путь до исполняемого файла запускаемого приложения должен передаваться в качестве аргумента. 

# При написании необходимо использовать модуль pywinauto.
# Пример запуска:
# test_app.py C:\Windows\system32\notepad.exe

from pywinauto import application
app = application.Application()
app.Start("Notepad.exe")
Wnd_Main = app.window_(title_re=".*Notepad")
Wnd_Main.Select("File")
t =Wnd_Main.SelectedTexts();
print(Wnd_Main.SelectedTexts())
Wnd_Main.close()

if t==Wnd_Main.SelectedTexts():
	print("it is open")
else:
	print("close")

