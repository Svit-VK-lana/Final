# Website for selling design services
#### Video Demo:  <https://youtu.be/Q9BPIwCTuko>
#### Description:


# Project Title

This website is intended to provide design services, to collect and store information about customers and to advertise the services provided.

In order to make a website, I used html, python, css and SQL.

For marking pages, creating the appearance of tables and request forms for placing photos and textual information, html was used.

With the help of CSS, various fonts and font sizes, element colors, indents of elements from each other, the location of individual blocks on the page, etc. were set for pages and individual elements.

In order for the site to behave differently in different situations, acting according to the prescribed algorithms, depending on the fulfillment or non-fulfillment of certain conditions. The ability to set the logic of the "behavior" of the site is the task of the python. Also, with this help, feedback is organized with customers, the collection and storage of information about customers and projects.

SQL - used to describe, modify and retrieve data about clients and projects.

Website navigation is made on the basis of the Budstrap template. The Flask framework is also used.  The website is adaptive, the image changes depending on the device on which the website is opened.

The site contains 4 pages for the client, 1 page for the administrator and 2 pages for messages about the success or failure of the order for design services

The main page contains information about the artist, his photo and buttons to go to other resources where artists exchange achievements, offer cooperation or sell finished works.

There are 2 buttons at the bottom of the page. By clicking on the first button, the client is redirected to an external resource that is designed to share experiences and advertise their own projects. When you click on the second button, a site opens where ready-made graphic works are offered for sale.

The second page is intended to showcase the different types of projects, graphic design samples and types of services that can be provided to the client. Under each sample there is a button that opens a new page and shows close-up details or industrial packaging options.

Also at the bottom of the page there is a button that redirects the client to a page where he is given the opportunity to make a charitable donation for the Ukrainian army in order to quickly defeat the Russian bandits in the aggressive war they started.

The third page is intended for interaction with the client, receiving and storing commercial information. With the help of SQL queries, the entered information is placed in the database.On the third page, the client has the opportunity to place an order. To do this, he needs to specify the type of project,specify deadlines and his contact details. If contacts are not specified, the client receives a warning and the order is not placed.

Information from the client is accepted in free form. The client can optionally indicate the type of project, deadline or full name and surname. But if the client has not decided on the type of project, then the order will still be placed, and the artist will discuss the details of the project personally at the meeting.
The only mandatory requirement is to provide contact information.


If the client has specified contact details, then the order is placed, the client receives a notification and all information is recorded in the database. SQL is used to record information in the database.

The admin page contains all information about orders, their current status, cost and deadlines
Information on the admin page is displayed using SKL requests.

The administrator, as necessary, adds information about the status of the order and its cost to the database.

The fourth page contains the artist's contact information.so that the client can contact the artist for advice on the project or to discuss requirements.

As a background, photos are placed on the pages of the site. On the page with a message about a successful order, a video serves as a background.
Style css file describes styles of fonts and pictures.

Information from the client is accepted in free form. The client can optionally indicate the type of project, deadline or full name and surname. But if the client has not decided on the type of project, then the order will still be placed, and the artist will discuss the details of the project personally at the meeting.
The only mandatory requirement is to provide contact information.

