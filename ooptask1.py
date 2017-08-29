class WrongTeamMember(Exception):
    pass

class Employee(object):
    def __init__(self, first_name, second_name, salary, experiance, manager):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.experiance = experiance
        self.manager = manager
        
    def get_salary(self):
        if self.experiance > 5:
            return self.salary * 1.2 + 500
        elif self.experiance > 2:
            return self.salary + 200
        else:
            return self.salary
    
    def __str__(self):
        return self.first_name + " " + self.second_name + ", manager: "\
                + self.manager.second_name + ", experiance: " + str(self.experiance)
        
class Designer(Employee):
    def __init__(self, first_name, second_name, salary, experiance, manager, effectivness):
        Employee.__init__(self, first_name, second_name, salary, experiance, manager)
        assert 0 < effectivness < 1, "effectivness coefficient(0-1)"
        self.effectivness = effectivness
        
    def get_salary(self):
        sal = Employee.get_salary(self)
        return sal * self.effectivness

class Manager(Employee):
    def __init__(self, first_name, second_name, salary, experiance, manager, team):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.experiance = experiance
        assert manager == "No manager", "Managers have no manger, thus use 'No manager'"
        self.manager = manager
        assert isinstance(team, list), "team should be a list type or just use empty list"
        self.team = team
        
    def get_salary(self):
        sal = Employee.get_salary(self)
        if len(self.team) > 10:
            sal += 300
        elif len(self.team) > 5:
            sal += 200
        temp = 0
        for empl in self.team:
            if isinstance(empl, Developer):
                temp += 1
        if temp > len(self.team) / 2:
            sal *= 1.1
        return sal
    
    def add_team_member(self, candidate):
        if isinstance(candidate, Developer) or isinstance(candidate, Designer):
            self.team.append(candidate)
        else:
            raise WrongTeamMember ("Only developers or designers can be in team")
        
    def del_team_member(self, candidate):
        for member in self.team:
            if candidate == member:
                self.team.remove(candidate)
                break
        else:
            return "No such member in team"
    
    def show_team(self):
        return self.team
    
    def __str__(self):
        return self.first_name + " " + self.second_name + ", manager: No manager"\
                + ", experiance: " + str(self.experiance)
        
class Developer(Employee):
    def __init__(self, first_name, second_name, salary, experiance, manager):
        Employee.__init__(self, first_name, second_name, salary, experiance, manager)
        

        
class Department(object):
    def __init__(self, managers):
        self.managers = managers
        
    def list_of_managers(self):
        for manager in self.managers:
            print(manager, end=' ')
            print("Team: ")
            for member in manager.team:
                print("--", end=' ')
                print(member)
    
    def give_salary(self):
        for manager in self.managers:
            print(manager.first_name + " " + manager.second_name +\
                  " got salary: " + str(round(manager.get_salary(), 2)))
            for employee in manager.team:
                print(employee.first_name + " " + employee.second_name + \
                " got salary: " + str(round(employee.get_salary(), 2)))
    
if __name__ == "__main__":
    m = Manager("G", 'H', 500, 8, "No manager", [])
    a = Developer("V", "G", 500, 7, m)
    m.add_team_member(a)
    b = Developer("S", "P", 900, 14, m)
    m.add_team_member(b)
    c = Developer("Q", "Q", 1000, 10, m)
    m.add_team_member(c)
    d = Developer("W", "W", 3500, 4, m)
    m.add_team_member(d)
    e = Developer("E", "E", 8000, 10, m)
    m.add_team_member(e)
    z = Designer("D", "S", 1500, 5, m, 0.9)
    m.add_team_member(z)
    dep = Department([m,])
    dep.give_salary()
    dep.list_of_managers()
    