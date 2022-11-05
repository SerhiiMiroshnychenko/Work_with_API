colors_dict = {
    "C++": 'gray',
    "C": 'gray',
    "Python": 'blue',
    "JavaScript": 'yellow',
    "TypeSkript": 'orange',
    "Vim Script": 'orange',
    "Shell": 'white',
    "": 'rgb(60, 100, 150)',
    "PowerShell": 'white',
    "PHP": 'purple',
    "Go": 'rgb(100, 150, 200)',
    "Jupiter Notebook": 'rgb(50, 50, 200)',
}

repo_names = ["C++", "C", "Python", "JavaScript", "TypeSkript", "Vim Script", "Shell",
              "", "PowerShell", "PHP", "Go", "Jupiter Notebook", "Java"]

for repo_name in repo_names:
    if repo_name in colors_dict:
        color = colors_dict[repo_name]
    else:
        color = 'rgb(25, 25, 25)'
    print(f"Мова: {repo_name}; Колір: {color}")

