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

    This command builds and saves the output to the **dist** folder.  
    Any changes made to the code after does not cause any change to the dist folder unless the ``ng build`` command is run again.

    4.2 ``ng serve``  
    ![ng serve](images/ng_serve.PNG)  

    The application is built and the output is saved to memory while the server is started.  
    This allows one to view the application on a web browser and it is available on port 4200 by default.  
    Any changes made in the code causes the application to be built again.  


5. **I understand the structure of an Angular component**  

    An Angular component is a JavaScript class that provides data to the view.    
    Many components come together to create the full UI displayed in the browser.   

    It is made up of 3 parts:  
    - Imports:   
    ![angular component structure imports](images/angular_component_structure_import.PNG)  
    This section imports the required libraries that would be useful in the class.  

    - Metadata:  
    ![angular component structure metadata](images/angular_component_structure_metadata.PNG)  
    It provides additional information about the component.  
     _@Component_ decorator is used to identify it.  

    - Class:  
    ![angular component structure class](images/angular_component_structure_class.PNG)  
    Made up of TypeScript/JavaScript code that provides the logic for the data displayed in the template.  


    An Angular component is usually stored as _nameOfComponent.component.ts_ file
    
6. **I can create components using Angular CLI**  

    6.1 ``ng generate component q5component``  
    ![ng serve](images/ng_serve.PNG)  

    The command creates a component.  
    A folder **q5component** is created under the **src/app** folder.  


7. **I can use Property Binding to control the state of a button**  

    In property binding, we need an HTML property, in our example **input's value property**.  
    We surround it with the square brackets _[  ]_ and assign its value to a property we have defined in out ts file _boolTrue/boolFalse_
    
    7.1 _Inside component's ts file_  
    ![q5component.component.ts](images/ng_property_build_component_ts.PNG)   

    7.2 _Inside component's html file_  
    ![q5component.component.html](images/ng_property_build_component_html.PNG)  

    7.3 _In the web browser_  
    ![In the web browser](images/ng_property_build_component_web_browser.PNG)  


8. **I can use Event Binding to invoke a function when a button is clicked**  

    Event Binding is a one-way data binding technique from view to the component.  
    It uses HTML events such as keystrokes, mouse clicks, etc to trigger methods that are defined in the component.  
    The event's name is wrapped inside _( )_ and the value is a method defined in the component class.  
    
    In my example, anytime a user clicks (event is click) on the _Submit_ button, the **clickSubmit()** function is called.  
    The function also calls an alert window which displays the text _Thank you, your details have been saved_  

    8.1 _Inside component's ts file_  
    <img src="https://github.com/maryjonah-turntabl/Foundations-Checklist/blob/main/angular/images/ng_event_binding_button_ts.PNG" width="600" height="350">

    8.2 _Inside component's html file_  
    <img src="https://github.com/maryjonah-turntabl/Foundations-Checklist/blob/main/angular/images/ng_event_binding_button_html.PNG" width="600" height="100"> 

    8.3 _In the web browser_  
    <img src="https://github.com/maryjonah-turntabl/Foundations-Checklist/blob/main/angular/images/ng_event_binding_button_browser.PNG" width="600" height="150">


9. **I can use Text Interpolation to display the value of a component string variable on that component???s view**  

    It is the use of the _{{}}_ to display dynamic content in an html page.  
    The data contained within the curly braces is referred to as a _template expression_.   
    This is a one-way data binding technique, where data is sent from the component to the view and cannot be the other way round.  
    The template expression can be an Angular _property, method, array or an object_.  

    9.1 _Inside component's ts file_  
    <img src="https://github.com/maryjonah-turntabl/Foundations-Checklist/blob/main/angular/images/ng_text_interpolation_ts.PNG" width="600" height="550">

    9.2 _Inside component's html file_  
    <img src="https://github.com/maryjonah-turntabl/Foundations-Checklist/blob/main/angular/images/ng_text_interpolation_html.PNG" width="600" height="220">    

    9.3 _In the web browser_  
    <img src="https://github.com/maryjonah-turntabl/Foundations-Checklist/blob/main/angular/images/ng_text_interpolation_browser.PNG" width="600" height="360">


10. **I understand the difference between Reactive Forms and Template-Driven Forms**  

    _Reactive Forms_:  
    Reactive Forms use the _ReactiveFormsModule_ in Angular.
    One has to apply the directive _formGroup_ and _formControl_ to the form and input elements in the html file since ngForm which would otherwise have automatically created a _FormGroup_ and _ngControl_ which also would have automatically created _FormControl_ is not applied when one is using ReactiveForm.

    

    _Template-Driven Forms_:  
    It uses the _FormsModule_ module in Angular.  
    These types of forms make the directives _NgForm_ and _NgModel_ and their associated selectors: _ngForm_, _ngSubmit_, and _ngModel_ available and they are used to capture the information in the form.  
    No additional imports are done in the component.ts file when one creates this kind of form.  
