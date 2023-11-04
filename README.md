
# Task - 1 : Excel File Uploader

## Instructions
- An excel file uploader which uploads files in a predefined format of your choice. You can upload it in any format.
- Once the format has been determined , the system  should upload the data to a MongoDB database. The data uploaded should be in a specifc mapped Format which would be done based on a screen where the user would select what type of data should go where. 

The uploaded file has the below columns:
- Product Name
- Description
- Type of Product (Fresh producde , Electronics , Games and toys)

Let`s say , our system works on a mapping which would be defined like this:

|  Type of Product | map to              |
| :----------------| :-------------------|
| Fresh Produce is mapped to | Standard Rate Type. |
| Electronics is mapped to   | Reverse charge |
| Games and toys             | GAT tax |

The system should provide a screen to the user where they can map Standard Rate , Reverse charge and GAT
TAX to types defined in the uploaded file (which in this case is Fresh Produce , Electronics and Games And
Toys).
Once this mapping has been saved , the system should then save the resultant mapped to a mongo DB with the
correctly mapped Types.

## project
A system have benn made to take .xlsx file in a given formet and it will take the data from the .xlsx file and store it to MongoDB.
It will show all the data in a table where user can change the mapping of each data in given options.
![image](https://github.com/TafhimFaisal/tax_star/assets/39499963/7e0a225f-9fcf-4a3c-865c-262a0de93bb4)

## Installations
navigte to task_1 folder and then open it in terminal 
and then run bellow command:

1. run ` python -m venv env `
2. run ` env/Scripts/activate `
3. run ` pip install -r requirements.txt `
4. made a .env file following the .env.example file.
5. run ` flask --app run --debug run `
6. opent browser in localhost:5000.
7. upload the given .xlsx file gien in project file to test.


# Task - 2 : XERO Integration Application
## Instructions
- The Task is to Create an Application with XERO API`s Fully Integrated with it . The Application can be created
using the coding language the company is looking for. The sub tasks of this application would be:
- Connect to a test Organization in XERO.
- After the connection has been established to a XERO org , pull in the data for the Accounts Module and show it
on a FrontEnd view.

## project
A system have benn made with intigration to xero. system has 3 navigation button 
1. landing page.
2. accout list page.
3. and enother button is for logout.
on starting the system will go to landing page. user need to go to account page to see dummy data fatch from xero applications.
before that you need to login with xero app to see the dumm data.

![image](https://github.com/TafhimFaisal/tax_star/assets/39499963/01354924-13d9-4fa0-ac2a-c26b24ef59f2)

## Installations
navigte to task_2 folder and then open it in terminal 
and then run bellow command:

1. run ` python -m venv env `
2. run ` env/Scripts/activate `
3. run ` pip install -r requirements.txt `
4. made a .env file following the .env.example file.
5. run ` flask --app app --debug run `
6. opent browser in localhost:5000.
7. upload the given .xlsx file gien in project file to test.



