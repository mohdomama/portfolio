import markdown
import requests

URLs = [
    ['https://raw.githubusercontent.com/mohdomama/VirtualStylus/master/README.md',
        'https://github.com/mohdomama/VirtualStylus'],
    ['https://raw.githubusercontent.com/mohdomama/AutonomousVehicle/master/README.md',
        'https://github.com/mohdomama/AutonomousVehicle'],
    ['https://raw.githubusercontent.com/mohdomama/HararaSpam/master/README.md',
        'https://github.com/mohdomama/HararaSpam']
]


# Better create a project class
def fetch_projects():
    md = markdown.Markdown()
    projects = []
    for url in URLs:
        project = []
        project.append(md.convert(requests.get(url[0]).text))
        project.append(url[1])
        # Making blockquote work with bootstrap
        project[0] = project[0].replace(
            '<blockquote>', '<blockquote class="blockquote">', )
        projects.append(project)
    return projects


def main():
    projects = fetch_projects()
    for project in projects:
        print(project[0])


if __name__ == '__main__':
    main()
