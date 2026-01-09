def format_name(Fname,Lname):
    """it take first name and last name as inputs and change it to title case

    Args:
        Fname (_String_): _type ur first name_
        Lname (_String_): _type ur last name_
    """
   
    fullName=Fname.title()
    lastName=Lname.title()
    
    print(f"{fullName} {lastName}")
    
    
format_name("ahmad","Naji")