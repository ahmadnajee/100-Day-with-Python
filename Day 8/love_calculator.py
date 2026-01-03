def love_score(name1,name2):
    name=name1+name2
    lower_name=name.lower()
    t=lower_name.count("t")
    r=lower_name.count("r")
    u=lower_name.count("u")
    e=lower_name.count("e")    
    true=str(t+r+u+e)
    l=name.count("l")
    o=name.count("o")
    v=name.count("v")
    E=name.count("e")
    love=str(l+o+v+E)
    love_scores=true+love       
    print(love_scores)    
    
    

love_score("Kanye West","Kim Kardashian")