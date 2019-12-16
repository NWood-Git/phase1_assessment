## Byte Academy Phase 1 Assessment

### Dec 2019

Answer the following questions. Open book and open internet, but you cannot ask
for assistance with code.

Place each answer in one of the answer sub-directories.

The in-class portion of the assessment is worth 60% of your grade. The take-home
portion is worth 40%. There is a 10% bonus question. A score of 70% passes. If
you score 60% you may turn in a fully corrected exam by the end of the following
day for 10% credit to pass.

Don't get stuck on any one problem. Move on and come back. Good luck!

#### 1: Zero Shift (10%)

Write a function called `zero_shift(a_list)`, it should take a list as its
argument and transform that list in-place, shifting all the zeros to the
right, but leaving the other elements in the same order. The function
should return None.

In a comment in your code, say what the time complexity (Big-O) of your algorithm is.

```python
my_list = [3, 0, 9, 10, 0, 1, 0, 7]

zero_shift(my_list)

print(my_list)

# outputs:

[3, 9, 10, 1, 7, 0, 0, 0]
```

For partial credit you may instead have the function return a new list that
has the elements from the argument in the zero-shifted order.

#### Question 2: Database (10%)

*You do not need to create classes for this question*

* Using python's sqlite3 module write a schema.py file that creates two database tables modeling the following:

    * Campuses: A campus has a city and a state.

    * Students: A student has a first name, a last name, and a GPA,

    * A campus has many students, a student has one campus.

* In a seed.py file, write python sqlite3 code to add two campuses for New York, NY and Houston, TX to the database. Insert the following students:

```
first, last, GPA

In New York, NY:

Lockett, Walker, 3.1
Coleman, Casey, 2.7
Kilome, Franklyn, 3.8
Santiago, Hecton, 2.9

In Houston, TX:

Valdez, Framber, 3.9
Peacock, Brad, 2.8
Guduan, Reymin, 3.5
Cole, Gerrit, 3.0
```

* After inserting the rows, update Franklyn Kilome's GPA to 2.5

* Write a python function that takes a city and state argument and returns the
average GPA for the students on that campus.

* Write a SQL SELECT statement to get the last names of all students in New York with a GPA over 3.0. Do not select based on an integer foreign key, use a join and select by the city name.

#### Question 3: Data Plot (10%)

* Run jupyter notebook from inside the problem 3 directory. Open the starter notebook.

* Load the Winemag csv data into a Pandas dataframe and create a scatter plot with x = price and y = points.

* Your work should be submitted as the ipynb file.

#### Question 4: Object Orientation (20%)

*This answer does not involve a database or the model classes from your projects*

Create classes that model the following heirarchy. Place each class in its own
python file.

##### Location

* A `Loction` has an `address` attribute. It is a string.

* Your init method should have an optional address argument that sets the address.

* Its string representation should look like `<Location: {address}>` such as `<Location: 1261 Wild Azalea Ln.>` 

##### Business

* A `Business` is a `Location`. It has a `name` attribute and a list of `Person` objects stored in a attribute called `employees`

* Home's init method should have an optional address argument. Use super to call Location's init method and then set `.employees` to be an empty list.

* It has a method, `add_employee(person)` that adds a new Person object to the employees list.

* It should have a string representation (use a `__double underscore method__`) that looks like `"{name}, {number of employees} employees"` like `"Gray's Papaya, 12 employees"`

##### Home

* A `Home` is a `Location`. It has a `residents` attribute. That is similar to `Business`'s `employees`

* Home's init method should have an optional address argument. Use super to call Location's init method and then set `.residents` to be an empty list.

* It has a `add_resident(person)` method that adds a new Person to `residents`.

* Its string representation is its address and the number of people living in the home, "1261 Wild Azalea Ln. 5 residents"

* It has a `.resident_names()` method that returns a **list of strings** of all of the `Person` objects in the `residents` list attribute converted into strings. (`str(a_person)` will return a person object's string representation).

* Bonus for no credit: Can you have a Home work as an iterator that yields the person objects from the `.residents` attribute? So you could write 

```python
# this is extra, you don't have to do this
for person in my_home:
    print(person.first_name)
```

##### Person

* A `Person` has a `first_name` and a `last_name` attribute.

* Its string representation (use a `__double underscore method__`) is "Lastname, Firstname"

##### run.py

* Create a run.py file that imports your classes and demonstrates the methods and attribute values of instances of the class.

#### Question 5: Unit Tests (10%)

Write unit tests for the Home and Business classes.

* You do not have to test string representations exactly, you can just confirm that return values are instances of string or contain instances of string.

* Have tests for each method outlined in the problem description for those two classes.

#### Bonus: github (+10%)

* Create an empty new github repo.

* Make it private and add your instructor as a collaborator. (You may ask for assistance on this part)

* Add that github repo as a remote to your assessment work.

* Push your work to that repo.
