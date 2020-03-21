from jinja2 import Template

def images():
    with open('images.html') as f:
        s = f.read()
    return s

def main():
    img_lst = [
        {'title': 'Simba thrown',
            'img': 'https://media.giphy.com/media/DvMHwFYLVHlZe/giphy.gif',
            'desc': 'Simba getting thrown'
        },
        {'title': 'Stone Campus',
            'img': 'https://stonecampus.net/img/weblogo.png',
            'desc': 'Good place to learn programming'
        },
        {'title': 'Peely',
            'img': 'https://www.androidcentral.com/sites/androidcentral.com/files/styles/w1600h900crop/public/article_images/2019/03/fortnite-peely-skin.jpg?itok=FwlTDd9K',
            'desc': 'Peely'
        }
    ]
    tmpl = Template(images())
    print(tmpl.render({'images' : img_lst}))

main()
