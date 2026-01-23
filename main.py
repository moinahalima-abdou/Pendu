from Modules.menu import menu

def main():
    try:
        menu()
    except Exception as e:
        print("Error", e)

main()