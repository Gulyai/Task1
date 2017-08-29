import unittest
from ooptask1 import Employee, Developer, Designer, Department, Manager, WrongTeamMember


class TestDepartment(unittest.TestCase):
    
    def setUp(self):
        #also checking for right attributes when crating instances of
        # classes: Developer, Designer, Department, Manager
        self.manager = Manager("Cool", 'Manager', 100, 2, "No manager", [])
        self.manager_team = [Developer("First", "Dev", 100, 1, self.manager), \
                           Developer("Second", "Dev2", 100, 5, self.manager), \
                           Developer("Third", "Dev3", 100, 10, self.manager),
                           Designer("First", "Desig", 200, 1.5, self.manager, 0.75)]
        for member in self.manager_team:
            self.manager.add_team_member(member)
        self.department = Department([self.manager,])
            
        
    def testAddTeamMember(self):
         self.manager.add_team_member(Developer("Fourth", "Dev4", 100, 0.5, self.manager))
         self.assertEqual(len(self.manager.team), 5)
         self.assertRaises(WrongTeamMember, self.manager.add_team_member, \
                           Manager("Cool", 'Manager', 100, 2, "No manager", []))
    
    def testEffectivness(self):
        try:
            self.manager_team[-1].effectivness
        except AttributeError:
            print("No attribute effectivness in class Designer")
    
    def testDelTeamMember(self):
        tester = self.manager.del_team_member
        tester(self.manager_team[2])
        self.assertEqual(len(self.manager.team), 3)
        self.assertEqual(tester(Designer("NoName", "Desig", 200, 1.5, self.manager, 0.75)), "No such member in team")
        
        
    def testEmployeeSalary(self):
         self.assertEqual(self.manager_team[0].get_salary(), 100)
         self.assertEqual(self.manager_team[1].get_salary(), 300)
         self.assertEqual(self.manager_team[2].get_salary(), 620)
         self.assertEqual(self.manager_team[3].get_salary(), 150)
         self.assertEqual(round(self.manager.get_salary()), 110)
         
         self.manager.add_team_member(Designer("First", "Desig", 200, 1.5, self.manager, 0.75))
         self.manager.add_team_member(Designer("First", "Desig", 200, 1.5, self.manager, 0.75))
         self.manager.add_team_member(Designer("First", "Desig", 200, 1.5, self.manager, 0.75))
         self.assertEqual(round(self.manager.get_salary()), 300)
         for x in range(4):
             self.manager.add_team_member(Designer("First", "Desig", 200, 1.5, self.manager, 0.75))
         self.assertEqual(round(self.manager.get_salary()), 400)
         
    def testManagerHaveNoManager(self):
        self.assertEqual(self.manager.manager, "No manager")
                
    def tearDown(self):
        self.manager = None
        print ("tearDown executed!")

if __name__ == "__main__": 
    unittest.main()
