import random

category_dict = {'category1': {}, 'category2': {}, 'category3': {}, 'category4': {}, 'category5': {}}


# saving project details
def saving_project_details(category_of_prog, category_det_dict):
    def find_and_save(cat):
        file1 = open("Project_details.txt", "r")
        lines = file1.readlines()
        details_to_store = [nested_dict for category_of_prog in category_det_dict.values() for nested_dict in
                            category_of_prog.values()]
        # saving category details

        file2 = open("Project_details.txt", "w")
        for line in lines:
            file2.write(line)
            for nested_dict in details_to_store:
                if cat in line:
                    file2.write("\n")
                    file2.write(str(nested_dict) + '\n')

        print(details_to_store)

    def error_1(cat):
        print("File not found.. Creating a new file...")
        file3 = open("Project_details.txt", "x")
        file3.write(cat + "\n")
        main()

    if category_of_prog == "category1":

        try:
            find_and_save("Category 1")

        except FileNotFoundError:
            error_1("Category 1")

        except ValueError:
            print("Category 1 is not found")
            find_and_save("Category 1")

        except Exception as e:
            print("An error occurred:", str(e))

    elif category_of_prog == "category2":

        try:
            find_and_save("Category 2")

        except FileNotFoundError:
            error_1("Category 2")

        except ValueError:
            print("Category 2 is not found")
            find_and_save("Category 2")

        except Exception as e:
            print("An error occurred:", str(e))

    elif category_of_prog == "category3":

        try:
            find_and_save("Category 3")

        except FileNotFoundError:
            error_1("Category 3")

        except ValueError:
            print("Category 3 is not found")
            find_and_save("Category 3")

        except Exception as e:
            print("An error occurred:", str(e))

    elif category_of_prog == "category4":

        try:
            find_and_save("Category 4")

        except FileNotFoundError:
            error_1("Category 4")

        except ValueError:
            print("Category 4 is not found")
            find_and_save("Category 4")

        except Exception as e:
            print("An error occurred:", str(e))

    elif category_of_prog == "category5":

        try:
            find_and_save("Category 5")

        except FileNotFoundError:
            error_1("Category 5")

        except ValueError:
            print("Category 5 is not found")
            find_and_save("Category 5")

        except Exception as e:
            print("An error occurred:", str(e))


# To clear and rewrite file
def clear_and_rewrite_file():
    # Open the file in write mode with 'truncate' option
    with open("Project_details.txt", "r+") as file:
        file.truncate(0)  # Truncate the file, removing all content

    with open("Project_details.txt", "w") as file:
        file.write("Category 1\nCategory 2\nCategory 3\nCategory 4\nCategory 5")


# Adding project details

def add_project_details():
    try:
        project_ID = int(input("Enter project ID: "))
        project_name = input("Enter project name: ")
        print()

        print("Category1 - Image Processing")
        print("Category2 - __________ ")
        print("Category3 - __________ ")
        print("Category4 - __________ ")
        print("Category5 - __________ ")

        category = input("Enter category (category1,category2,category3,category4,category5): ")

        team_members = []
        no_of_team_members = int(input("Enter the number of team members: "))
        for i in range(no_of_team_members):
            member_name = input("Names of team members: ")
            team_members.append(member_name)

        description = input("Enter a brief description about project: ")
        country = input("Enter the country: ")

        project_details = {
            "project_ID": project_ID,
            "project_name": project_name,
            "category": category,
            "team_members": team_members,
            "description": description,
            "country": country
        }

        category_dict[category][project_ID] = project_details

        print("Project details added successfully!")

        return category, project_details
    except ValueError:
        print("Invalid Input")
        main()


# Load project details from text file to the dictionary

def load_project_details():
    try:
        new_category_dict = {}
        current_category = None

        file = open("Project_details.txt", "r")
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line.startswith("Category"):
                current_category = line.replace(" ", "").lower()
                new_category_dict[current_category] = {}
            elif line.startswith("{"):
                project_details_dict = eval(line)
                if current_category is not None:
                    project_id = project_details_dict.get('project_ID')
                    if project_id is not None:
                        project_id = int(project_id)
                        new_category_dict[current_category][project_id] = project_details_dict
                    else:
                        print("Project ID not found for a project.")
                        pass
                else:
                    print("No current category.")

        # clear_and_rewrite_file()

        return new_category_dict
    except FileNotFoundError:
        print("Project details file not found.")


# Deleting project details
def delete_project_details():
    try:
        new_category_dict = load_project_details()

        project_id = int(input("Enter Project ID: "))

        # print(new_category_dict)
        for category, projects in new_category_dict.items():
            # Check if the project ID exists in the current category
            if project_id in projects:
                # If found, delete the project
                del new_category_dict[category][project_id]
                print("Item deleted successfully")
        else:
            print("project_id not found")

        return category, new_category_dict
    except ValueError:
        print("Invalid Project ID format")
        main()


# Updating project details
def update_project_details():
    try:
        # while True:
        new_category_dict = load_project_details()
        project_id = int(input("Enter Project ID: "))

        # Check if project ID exists in any category
        for category, projects in new_category_dict.items():
            if project_id in projects:
                # If found, get the project details
                project_details = new_category_dict[category][project_id]

                # Prompt user for new details
                print("----- To Update -----")
                print("project_ID       -----> Enter 1")
                print("project_name     -----> Enter 2")
                print("category         -----> Enter 3")
                print("team_members     -----> Enter 4")
                print("new_description  -----> Enter 5")
                print("new_country      -----> Enter 6")
                print("All details      -----> Enter 7")

                key_to_update = int(input("Enter what do you want to update: "))

                if key_to_update == 1:
                    project_details['project_ID'] = int(input("Enter new project ID: "))
                elif key_to_update == 2:
                    project_details['project_name'] = input("Enter new project name: ")
                elif key_to_update == 3:
                    project_details['category'] = input("Enter new project category: ")
                elif key_to_update == 4:
                    project_details['team_members'] = input("Enter new team members (comma-separated): ").split(',')
                elif key_to_update == 5:
                    project_details['description'] = input("Enter new description: ")
                elif key_to_update == 6:
                    project_details['country'] = input("Enter new country: ")
                elif key_to_update == 7:
                    new_id = int(input("Enter new project ID: "))
                    new_name = input("Enter new project name: ")
                    new_category = input("Enter new project category: ")
                    new_team_members = input("Enter new team members (comma-separated): ").split(',')
                    new_description = input("Enter new description: ")
                    new_country = input("Enter new country: ")

                    # Update the project details
                    project_details['project_ID'] = new_id
                    project_details['project_name'] = new_name
                    project_details['category'] = new_category
                    project_details['team_members'] = new_team_members
                    project_details['description'] = new_description
                    project_details['country'] = new_country

                else:
                    print("yes")
                    print("Invalid input")

                new_category_dict[category][project_id] = project_details
                print("Item updated successfully")

        return category, new_category_dict

    except ValueError:
        print("Invalid Project ID format")
        main()


def viewing_project_details():
    new_category_dict = load_project_details()

    project_IDs_lst = []
    sorted_temp_dict = {}

    for category, projects in new_category_dict.items():
        for project_id, details in projects.items():
            project_IDs_lst.append(details['project_ID'])

    for i in range(1, len(project_IDs_lst)):
        pid = project_IDs_lst[i]
        j = i - 1
        while j >= 0 and pid < project_IDs_lst[j]:
            project_IDs_lst[j + 1] = project_IDs_lst[j]
            j = j - 1
        project_IDs_lst[j + 1] = pid

    for pid in project_IDs_lst:
        for category, projects in new_category_dict.items():
            for project_id, details in projects.items():
                if details['project_ID'] == pid:
                    if category not in sorted_temp_dict:
                        sorted_temp_dict[category] = {}
                    sorted_temp_dict[category][project_id] = details
    for category, projects in sorted_temp_dict.items():
        new_category_dict[category] = projects

    for key, value in new_category_dict.items():
        for id, detail in value.items():
            print(detail)


def exit_sys():
    choice = input("Do you want to exit? (yes/no): ")
    if choice.lower() == 'yes':
        quit()
    elif choice.lower() == 'no':
        main()
    else:
        print("Invalid input")


def random_spotlight_selection():
    new_category_dict = load_project_details()

    selected_projects = {}

    # Iterate over each category
    for category, projects in new_category_dict.items():
        # Check if the category has projects
        if len(projects) > 0:
            # Select a random project from the category
            random_project_id = random.choice(list(projects.keys()))
            selected_projects[category] = projects[random_project_id]

    # Display the randomly selected projects
    for category, project_details in selected_projects.items():
        print(f"Category: {category}")
        print("Randomly Selected Project Details:")
        print(project_details)
        print()

    return selected_projects
def award_winning_projects():
    selected_projects = random_spotlight_selection()
    award_dict = {}
    for key, value in selected_projects.items():
        print("Points for", key, "project")
        # Input points from judges for each project
        judger1 = list(input("Enter points (out of 5) as * from 1st judger for this project: "))
        judger2 = list(input("Enter points (out of 5) as * from 2nd judger for this project: "))
        judger3 = list(input("Enter points (out of 5) as * from 3rd judger for this project: "))
        judger4 = list(input("Enter points (out of 5) as * from 4th judger for this project: "))

        def del_empty_elements(judger):
            i = len(judger) - 1
            while i >= 0:
                if judger[i] == ' ':
                    del judger[i]
                i -= 1


        del_empty_elements(judger1)
        del_empty_elements(judger2)
        del_empty_elements(judger3)
        del_empty_elements(judger4)

        points = len(judger1) + len(judger2) + len(judger3) + len(judger4)

        award_dict[value['project_ID']] = {
            'points': points,
            'name': value['project_name'],
            'country': value['country']
        }

    # Convert dictionary items to a list of tuples
    items = list(award_dict.items())

    # Implementing selection sort algorithm to sort the list of tuples in descending order based on values
    n = len(items)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if items[j][1]['points'] > items[max_index][1]['points']:
                max_index = j
        # Swap the maximum value with the current value
        items[i], items[max_index] = items[max_index], items[i]

    # Convert the sorted list of tuples back to a dictionary
    sorted_dict = dict(items)

    return sorted_dict


#award_winning_projects()

def visualizing():
    sorted_dict = award_winning_projects()

    points_list = []
    name_list = []
    country_list = []

    for key, value in sorted_dict.items():
        points = value['points']
        name = value['name']
        country = value['country']

        points_list.append(points)
        name_list.append(name)
        country_list.append(country)

    for i in range(1, points_list[0]):
        x = "*"
        print(x)

        if i == (points_list[0] - points_list[1]):
            x = x + " " * 50 + "*"
            for j in range(1, points_list[1]):
                print(x)

                if j == (points_list[1] - points_list[2]):
                    x = x + " " * 50 + "*"
                    for k in range(points_list[2]):
                        print(x)
                    break
            break

    max_length = 0
    for i in range(3):
        name_length = len(name_list[i])
        if name_length > 0:
            max_length = name_length

    for j in range(3):
        new_name = name_list[j] + " " * (40 - (max_length + 14))
        print("Project Name: " + new_name, end='')
        # new_name_list.append("Project Name: " + new_name)
    print()
    max_length = 0
    for i in range(3):
        country_length = len(country_list[i])
        if country_length > 0:
            max_length = country_length

    for j in range(3):
        new_country = country_list[j] + " " * (40 - (max_length + 9))
        print("Country: " + new_country, end='')


def main():
    print("__________Welcome__________")
    print("Option1: Adding Project details      ----> Enter 1")
    print("Option2: Deleting Project details    ----> Enter 2")
    print("Option3: Updating Project details    ----> Enter 3")
    print("Option4: Viewing Project details     ----> Enter 4")
    print("Option5: Random Spotlight Selection  ----> Enter 5")
    print("Option6: visualizing                 ----> Enter 6")
    print("Option7: Exit                        ----> Enter 7")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("__________Adding Project details__________")

        while True:
            category, project_details = add_project_details()
            choice = input("Do you want to add another project? (yes/no): ")
            if choice.lower() != "yes":
                saving_project_details(category, category_dict)
                main()

    elif choice == 2:
        print("__________Deleting Project details__________")

        while True:
            category, new_category_dict = delete_project_details()
            choice = input("Do you want to delete another project? (yes/no): ")
            if choice.lower() != "yes":
                clear_and_rewrite_file()
                saving_project_details(category, new_category_dict)
                main()

    elif choice == 3:
        print("__________Updating Project details__________")
        while True:
            category, new_category_dict = update_project_details()
            choice = input("Do you want to update another project? (yes/no): ")
            if choice.lower() != "yes":
                clear_and_rewrite_file()
                saving_project_details(category, new_category_dict)
                main()

    elif choice == 4:
        print("__________Viewing Project details__________")
        viewing_project_details()

    elif choice == 5:
        print("__________Random Spotlight Selection__________")
        random_spotlight_selection()

    elif choice == 6:
        print("__________visualizing__________")
        visualizing()

    elif choice == 7:
        print("__________Exit__________")
        exit_sys()

    else:
        print("Invalid input")

main()
