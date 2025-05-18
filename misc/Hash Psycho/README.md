# 🧠 Hash Psycho – CTF Write-up
![image](https://github.com/user-attachments/assets/518c3ac4-407c-4450-b033-b45920f63c74)

---

## 📜 Challenge Description

> Brand new authentication server, zero security vulnerabilities.

---

## 🔍 Objective

Bypass the authentication system and access the admin's office by forging a user object with a matching hash value to the admin's.

---

## 📂 Source Code Analysis

We are provided with a Python file that creates a `User` class and assigns an admin user with ID `1337`.

```python
ADMIN = User('admin', 1337)
```

```python
if hash(YOURUSER) == hash(ADMIN):
    print(FLAG)
```
---
## 🧠 Python Hash Insight
In CPython (64-bit), the hash() function for integers is implemented as:
```python
hash(x) == x % (2**61 - 1)
```
This allows us to create a collision:
```python
forged_id = 1337 + (2**61 - 1)
```
Result:
```python
>>> 1337 == hash(1337 + (2**61 - 1))
```
True
So, even though the ID isn't 1337, the hash value is the same — exactly what we need.
The forged id is 2305843009213695288

Flag - byuctf{wh0_kn3w_h4sh_w4snt_h4sh}
