import random

def handle_response(msg) -> str:
    p_msg = msg.lower()

    if p_msg == 'hello':
        return "你好"

    if p_msg == "roll":
        return str(random.randint(1,6))

    if p_msg == "help":
        return "This is a help message that you can modify."
    
    if p_msg == "选傻逼":
        list = ["金穆熙","周异","卓伟达"]
        random_element = random.choice(list)
        return(f"傻逼就是: {random_element}")


    