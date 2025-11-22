# **Object-Oriented Programming (OOP) in Python – Complete Guide with Examples**

This project demonstrates all major types of inheritance and object-oriented concepts in Python, using simple, easy-to-understand examples.
Each section includes code, output, and a graphical inheritance diagram.

---

## 🧱 **1. Class & Object Example**

A basic implementation of a `Student` class with attributes and methods.

### **Concepts Covered**

* Class
* Object Creation
* Constructor (`__init__`)
* Instance Variables
* Methods

---

## 🐶 **2. Single Level Inheritance**

Example: `Animal → Dog`

Dog inherits properties of Animal.

### **Diagram**

```
   ---------
   |Animal|
   ---------
       |
   --------
   | Dog  |
   --------
```

---

## 🧑‍💼 **3. Multilevel Inheritance**

Example: `Person → Employee → Manager`

Manager indirectly inherits from Person through Employee.

### **Diagram**

```
   ---------
   |Person|
   ---------
       |
   ----------
   |Employee|
   ----------
       |
   ----------
   |Manager|
   ----------
```

---

## 👨‍👩‍👦 **4. Multiple Inheritance**

Example: `Father` + `Mother` → `Child`

Child inherits from both parents.

### **Diagram**

```
   ---------     ---------
   | Father |    | Mother |
   ---------     ---------
        \         /
         \       /
        ----------
        | Child |
        ----------
```

---

## 🏢 **5. Hierarchical Inheritance**

Example:
Base class: `Company`
Derived classes: `HP`, `Dell`

### **Diagram**

```
       ----------
       |Company|
       ----------
        /      \
       /        \
   -------    -------
   | HP  |    |Dell|
   -------    -------
```

---

## 👴👨👩👦 **6. Hybrid (Multiple + Hierarchical) Inheritance**

This is the advanced example combining all concepts.

### **Classes Involved**

* `Grandfather`
* `Father` (inherits from Grandfather)
* `Mother` (inherits from Grandfather)
* `Child` (inherits from Father & Mother)

### **Key Features**

* Uses Python’s **MRO (Method Resolution Order)**
* Uses `super()` properly with `**kwargs` for cooperative initialization
* Demonstrates how constructors behave in multiple inheritance

### **Diagram**

```
         --------------
         | Grandfather |
         --------------
           /        \
          /          \
     ----------   ----------
     | Father |   | Mother |
     ----------   ----------
          \         /
           \       /
          ----------
          | Child |
          ----------
```

---

## 📌 **Final Output Example**

```
I am Child
Grandfather Name: Robert, Place of Birth: New York
Skills: Fishing, Gardening
Father Age: 50
Skills: Programming, Cooking
Mother Age: 48
Skills: Art, Crafting
Child Skills: Sports, Dancing
```

---

## 📚 **Concepts Demonstrated in This Project**

* Classes & Objects
* Constructors (`__init__`)
* Method Overriding
* Inheritance Types:

  * Single Level
  * Multiple
  * Multilevel
  * Hierarchical
  * Hybrid
* `super()` in single and multiple inheritance
* Python’s MRO (Method Resolution Order)
* Cooperative Multiple Inheritance using `**kwargs`

---

## 🚀 How to Run

1. Save the code in any Python file, e.g., `oops_examples.py`
2. Run:

```
python first.py
```

---

## ⭐ Author

**Ashish (Anticoder03)**
Loves coding & anime | BCA Student | Python & Web Dev Enthusiast

