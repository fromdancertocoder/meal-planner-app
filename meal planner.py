pantry = {"pasta" : 1, "mushrooms" : 10}
grocery_list = {}
meal_plan = []
meals_names = ["pasta bake", "roast chicken"]
meal_count = 1
meals = []
class Meal:
  def __init__(self, name = " ", servings = 0, ingredents = {}):
    self.name = name
    self.servings = servings
    self.ingredents = ingredents
    meals.append(self)
  def __repr__(self):
    return "{}".format(self.name)  
  def plan_meal(self):
    for item in self.ingredents:
      if item in stock: 
        total = stock[item]
        if total - self.ingredents[item] < 0:
          grocery_list[item] = self.ingredents[item] - total
          stock[item] = 0 
        if total - self.ingredents[item] >= 0:
          stock[item] -= self.ingredents[item]
      elif item in grocery_list:
        grocery_list[item] += self.ingredents[item]    
      else: grocery_list[item] = self.ingredents[item]    
    days = self.servings / 2
    while days > 0: 
      meal_plan.append(self.name)
      days -= 1 
 
meal1 = Meal("pasta bake", 4, {"pasta" : 1, "pasta sauce" : 1, "sausage" : 1, "mushrooms" : 2})
meal2 = Meal("roast chicken", 2, {"chicken breast" : 2, "carrots" : 1, "potatoes" : 1})
for x in range(3, 99):
  globals()[f"meal{x}"] = Meal()

forever = 1
while forever > 0:
  choice_1 = int(input("Welcome to your full service meal planning app \n What are we doing today? \n 1. planning a meal \n 2. stocking the pantry \n 3. cooking a meal \n 4. ate a meal \n 5. show meal plan \n 6. new recipe \n 7. show pantry \n "))
  if choice_1 == 1:
    stock = pantry.copy()
    count = 1
    while count > 0:
      meal = input("Which meal would you like to add to the menu {l} \n type end to stop\n ".format(l = meals_names))
      if meal =="end": 
        count -= 1
        print("Your grocery list is {l}".format(l = grocery_list))
        print("your meal plan is {p}".format(p = meal_plan))
        continue
      ind = meals_names.index(meal)
      (meals[ind]).plan_meal() 
  if choice_1 == 2:
    count = 1
    while count > 0:
      new_item = input("what did you buy at the store? type end to stop\n ")
      if new_item == "end": 
        count -= 1
        continue
      new_amount = int(input("how many/much did you buy?\n "))
      if new_item in pantry:
        pantry[new_item] += new_amount
      else: pantry[new_item] = new_amount  
    print("your items have been added to the pantry")  
  if choice_1 == 3:
    cooked_meal = input("what meal did you cook {n} \n ".format(n = meals_names))
    ind = meals_names.index(cooked_meal)
    cooked = meals[ind]
    for item in cooked.ingredents:
      pantry[item] -=  cooked.ingredents[item]
    print("the ingredents for {c} hav been remove from the pantry".format(c = cooked.name))  
  if choice_1 == 4:
    consumed = input("what did you eat? {plan} \n ".format(plan = meal_plan))
    meal_plan.remove(consumed)
    print("{m} has been remove from the meal que".format(m = consumed))
  if choice_1 == 5:
    print("you next {l} meal are {mp}".format(l = len(meal_plan), mp = meal_plan))
  if choice_1 == 6:
    meal_count += 1
    meals[meal_count].name = input("whats your new recipe called? \n ")
    meals[meal_count].servings = int(input("How many does it serve? \n "))
    count = 1 
    while count > 0:
      new_ingredent = input("name an ingredent \ntype end to stop \n  ")
      if new_ingredent == "end":
        count -= 1
        continue
      new_value = int(input("how many/much? \n "))
      meals[meal_count].ingredents[new_ingredent] = new_value 
    meals_names.append(meals[meal_count].name)
    print("new recipe {n}".format(n = meals[meal_count].name))  
  if choice_1 == 7:
    print(pantry) 