def secret_me():
    print("   /' `\\                                                                              ")
    print("       /'   ._)                                                                         ")
    print("      (____    ____     ____     ____     ____     ,__________         ,__________     ____ ")
    print("           ) /'    )--)'    )--/'    )  /'    )   /'    )     )       /'    )     )  /'    )")
    print("         /'/'       /'       /(___,/' /'    /'  /'    /'    /'      /'    /'    /' /(___,/' ")
    print("(_____,/' (___,/  /'        (________(___,/(__/'    /'    /(__    /'    /'    /(__(________ ")
    print("                                                                                            ")

    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() in ['yes', 'y']:
        print("Access granted.")
        import main
        main
        return None
    else:
        print("Access denied.")

secret_me()
