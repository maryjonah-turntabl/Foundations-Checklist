## Version Control with Git

1. **I understand the elements of Git workflow (working directory -> staging area -> local repo -> remote repo**

    1.1 Working directory
    
    It is a folder that contains or will contain your git files.   
    Applying the ``git init`` command inside of it makes it a _git repository_.

    1.2 Staging area

    When a working directory is initialized and we make changes to the files it contains.      
    Next we need to store the changes made to an area before they are committed.  
    And the area is called the staging area.  
    ``git add nameOfFile``, ``git add .`` are used to add either a single file or all the files that have been changed to the staging area. 

    1.3 Local repo

    This is an area on your computer where changes are stored.  
    Initially a working directory is initialized, and files are added to the staging area.  
    Next, the files are committed to the local repository using the ``git commit`` command.  
    One does not also need Internet connection to store changes to the local repository.


    1.4 Remote repo

    This is a repository that is not hosted on your computer.
    You may need Internet access to store files on the remote repository.


  
2. **I can initialise Git repositories**

    2.1 ``git init``  
    ![git init output](/images/git_init.PNG)

    Is used to initialize a repository.  
    It creates a _.git_ hidden folder.



3. **I can create a new branch and check it out**

    3.1 ``git checkout -b ttlab1Branch``  
    ![git checkout -b ttLab1 output](/images/git_checkout_b.PNG)

    A combination of the commands ``checkout`` and ``b`` to create a new branch.  
    And the command switches the current user to now work and save changes in the new branch.



4. **I can stage changes and commit them to my branch**

    4.1 ``git add ttLabFile.txt`` adds the file ttLabFile.txt to the staging area  
    4.2 ``git commit -m "Q4"`` commits the file to the local repository  
    ![git add & commit -m output](/images/git_add_commit_m.PNG)



5. **I can write meaningful commit messages that are useful for other developers** 

    5.1 _Answer Q4_, _Create component dashboard_, _Merge branch dev_  
    ![git commit -m "Answer Q4"](/images/git_commit_m_answer_q4.PNG)

       5.1.1 Use imperative mood to write git messages.  
       5.1.2 Apply continue your messages to the phrase "If applied, this commit will ...." to check if it is meaningful.



6. **I can push the changes committed to my local branch to the remote branch** 

    6.1 ``git push ``  
    ![git push"](/images/git_push.PNG)

    It send changes to the current branch ``git`` to its corresponding remote branch which assumes already exists.



7. **I can check the status of my branch and understand the output**  

    7.1 ``git status``  
    ![git status"](/images/git_status.PNG)  

    The output shows that the content of the file _README.md_ has changed.  
    The file has not been placed in the staging area.  
    So a suggestion of using ``git add`` to include it in the staging area or using ``git commit -a`` stages and commits the change to the local repository



8. **I can switch branches**

    8.1 ``git checkout main``  
    ![git checkout main"](/images/git_checkout_main.PNG)  

    It changes the branch from the current ``git`` to the default branch ``main``



    
