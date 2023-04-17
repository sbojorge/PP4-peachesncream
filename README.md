![Peachesncream logo]

<!-- Ideally replace the code institute logo with the one for your application -->

# Peaches 'n cream


This is a grocery shopping list application that, as its [meaning](https://dictionary.cambridge.org/dictionary/english/peaches-and-cream) in informal english states, is expected to be pleasant and easy.<br>
It'll be useful for users searching to organize their trips for groceries.
The application lets the user create, read, update and/or delete grocery shopping lists. <br>
List won't be lost nor forgotten, but instead will be right at user's finger tips in his/her mobile.<br>
<br>

<!-- Add an image of the responsive app here and underneath this the link to the deployed app. -->

## Contents
<!-- I've writen this content for helping to organize and follow the README and TESTING content. As GitHub creates automatically a table content after 2 or more headings, I'll probably delete this content once the README will be completed. -->

1. [Technologies](#technologies)
2. Methodology
    - Themes, Epics and User stories
    - Backlog refinement
    - Kanban board    
3. Design
    - Database schema
    - Wireframes (Mobile and desktop)
    - Typography
    - Colors
    - Images?
4. Features
    - Existing features
    - Features to be implemented
5. Testing
    - Markdown validator
    - CSS validator
    - JS Hint
    - CI Python linter
    - Responsiveness
    - Accesibility
    - Lighthouse
    - Manual and/or Automated testing
6. Deployment
7. Credits
    - Content
    - Media
8. Acknowledgments

[Back to top 🔺](#peachesncream)

------

### Technologies
<!-- Currently showing here some examples of technologies that I'll probably use. Develop a bit for each of them as shown below for balsamiq -->
* HTML
* CSS
* Bootstrap
* GitHub
* Font Awesome
* Convertio
    * Images were converted to WEBP format using [Convertio](https://tinyjpg.com/) 
* Resize
    * Images were resized using [Resizepixel](https://www.resizepixel.com/)
* TinyJPG
    * Images were compressed using [TinyJPG](https://tinyjpg.com/)
* Favicon.io    
* Balsamiq
    * Wireframes were created using [Balsamiq Wireframes for desktop](https://balsamiq.com/wireframes/desktop/)
 * Canvas
    * For creating the logo at [Canvas](https://www.canva.com/)

[Back to top 🔺](#peachesncream)

------

### Methodology
The methodology used in this project is the Kanban Agile management methodology.

It was put in place using different functionalities in GitHub: 
* Issues, for the user stories; <!-- add pic -->
* Milestone (without due date), for the product backlog; <!-- add pic -->
* Milestone (WITH due date), for each iteration; <!-- add pic -->
* Project, for the Kanban board. I created a project per iteration. <!-- add pic -->
> Kanban is an Agile management method built on a philosophy of continuous improvement, where work items are “pulled” from a product backlog into a steady flow of work. The framework is applied using Kanban boards—a form of visual project management. In a Kanban board, tasks—represented as cards—move through stages of work—represented as columns...“To do,” “In progress,” and “Done.” Each column is filled with visual cards that represent individual tasks. A team moves through the columns until the tasks are completed.

<!-- Add a project picture here. -->

------

[Back to top 🔺](#peachesncream)

### Design
#### Database schema
##### Wireframes
* Mobile
* Desktop
#### Typography
#### Colors
#### Images

------

[Back to top 🔺](#peachesncream)

### Features

------

### Testing

------

### Deployment

The application was early deployed following these steps:

* Prepare environment and settings.py file
    -   create env.py,
    -   secret key,
    -   database url and update the database section,
    -   cloudinary url, link Cloudinary to the application for storing media and static files and add the cloudinary apps in the installed apps section
    -   templates including creating the corresponding directory, 
    -   allowed host,    
    
* Create an external database on ElephantSQL and attach it to the application
* Create an application on Heroku and prepare the configuration variables on it
    -   secret key
    -   database url
    -   cloudinary url
    -   port
    -   disable collectstatic

* Create media and static directories
* Create and prepare a procfile
* Connect the repository to the Heroku app and deploy branch

The application was successfully deployed at the first attempt.


### Credits
#### Content
* Quotation about the Kanban management methodology: visit https://asana.com/resources/what-is-kanban

[Back to top 🔺](#peachesncream)
