from jinja2 import Template

def my_items():
    with open('items.html') as f:
        s = f.read()
    return s

def main():
    items_lst = [
        {'name' : 'orange', 'cnt': 100},
        {'name' : 'apple', 'cnt': 75},
        {'name' : 'banana', 'cnt': 30}
    ]
    tmpl = Template(my_items())
    print(tmpl.render({'items' : items_lst}))

main()

