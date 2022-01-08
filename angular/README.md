## Angular

1. **I understand the structure of an Angular application**

    ![Angular structure](images/angular_structure.PNG)
    
    An Angular application is made up of a series of files and folders.  
    I would like to talk about the following:  
    - _src/_ : Folder contains the components and services that will make up the UI and fetch data to be displayed in the case where we need to get it from an external source.  
    - _README.md_: Readme file that contains commands on how to run and test the Angular application.  
    - _node\_modules_: Folder that contains the required node modules needed to build the application.    



2. **I understand what a Single Page Application is**

    This is when a website does not go back and forth to the server anytime a user requests for information.
    There are no frequent reloads to the website as the request for information done behind the scene and only parts of the website that have new information are updated and not the whole page.  



3. **I can create a new Angular application using Angular CLI**

    3.1 ``ng new ttAngular``  
    ![ng new ttAngular](images/ng_new_ttAngular.PNG)

    The command above is used to create a new Angular application by name _ttAngular_


4. **I can build and serve an Angular application using Angular CLI**  

    4.1 ``ng build``  
    ![ng build](images/ng_build.PNG)  

    This command builds the application into the **dist** folder.  
    Any changes made to the code after does not cause any change to the dist folder unless the ``ng build`` command is run again.

    4.2 ``ng serve``  
    ![ng serve](images/ng_serve.PNG)  

    It starts your web browser and your application is available on the specified port (4200 by default).  
    Any changes made in the code causes the application to be built again.


5. **I understand the structure of an Angular component**  

    The idea behind a component is creating a custom browser tag and adding functionality that says what it does.  
    A component is made up of a decorator ``@Component`` and a class both which are defined in a **nameOfComponent.component.ts** file.  


6. **I can create components using Angular CLI**  

    6.1 ``ng generate component q5component``  
    ![ng serve](images/ng_serve.PNG)  

    The command creates a component.  
    A folder **q5component** is created under the **src/app** folder.  


