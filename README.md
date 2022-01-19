# MIT-WPU Octathon 2022
---
# Team Syntax Terminators (Octa_12)

Live Web-App :- https://secure-site.herokuapp.com/

--- 

![result 0](https://i.ibb.co/B6yrWfc/Screenshot-Securesite.png)

---

## Domain :- CyberSecurity
---
## Project Name:- SecureSite
---
## Problem Statement :-
(PS_01) Phishing website detecting software:-

Phishing is one of the techniques which are used by intruders to get access to the user credentials or to gain access to sensitive data. This type of access is done by creating a replica of the websites which looks the same as the original websites which we use on a daily basis but when a user clicks on the link he will see the website and think it's original and try to provide his credentials.

To overcome this problem we are using some of the machine learning algorithms in which will help us to identify the phishing websites based on the features present in the algorithm. By using this algorithm we can be able to keep the user personal credentials or sensitive data safe from intruders.

---

## Objective :-
 The main aim of the project to provide users with an interactive interface using which they can predict if a website is phishing or not.
 
 We will extract the features from the given URL and give them to our model for predictions. We are going to compare different machine learning algorithms and the best classifier that will be used to detect malicious URL .
 
 ---
## Dataset :-
To evaluate our machine learning techniques, we have used the ‘Phishing Websites Dataset’ from the UCI Machine learning repository.  It consists of features of 11055 URLs. Each URL has 30 Features/Attributes .

Link of Dataset :- https://archive.ics.uci.edu/ml/datasets/Phishing+Websites

---
## Algorithms used are :-
- Random Forest Classifier ( Accuracy = 97.4% )
- K-Nearest Neighbours (KNN) ( Accuracy = 95% )
- Naive Bayes Classifier ( Accuracy = 90% )
- Logistic Regression ( Accuracy = 92.6% )
- Artificial Neural Networks ( Accuracy = 96% )

---
## Installation

Create a virtualenv and install the dependencies.

In macOS and Linux:
```sh
virtualenv env
source test/Scripts/activate
pip install -r requirements.txt
```
In Windows:
```cmd
python3 -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```
Then change directory:
```sh
cd securesite/
```
To run...
```sh
python manage.py runserver
```
<hr>

## Example Sites:
```sh
(Secure Sites)
- hackmitwpu.com
- erp.mitwpu.edu.in

(Phishing Sites)
~ 2020logs.duckdns.org
~ 109.197.125.34.bc.googleusercontent.com

```


## Contributers 
 * [Kanishk Jamgaonkar](https://github.com/kanishk7559)
 * [Nidhi Sabu](https://github.com/blurryface-1)
 * [Muhammad Arab](https://github.com/muhammmadarab)
