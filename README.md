[![Build Status](https://travis-ci.org/Lemoenskil/E-commerce-webpage-staraid.svg?branch=master)](https://travis-ci.org/Lemoenskil/E-commerce-webpage-staraid)

# E-commerce-website-Staraid

This web application has been designed and built for the requirements of the "E-commerce-website" project of the Code Institute Full-Stack Software Development course.  It is intended to be used as a  e_comerce website where you can buy the product,
and  the process from order to shipment.  Which will include a chart, payment, shipping and for the future invoicing.   There will also be a support which will be for before and after sales.
Staraid is a autoguider that is used when you are tracking stars for astrofotograpy it is a higly texhnical product and is intended to make life easier for the not that techinical or entered astrofototographer.
As it is nich market mostly focus on hobbiest the website will need to have a lot of infromation on it.  They will also be searching for review or current users as it is a pricy product it will not be a impulse buy.
There will also be extra product availbe that the customer can buy that is needed for his setup and addons for StarAid.  For the future a blog will be place where the more experience customer can share his photo and give user tips new customer
in this to try  buld a the brand name.  The website will also have a facebook link where we will share system updates and happy customer blogs.  The website will also be use for support for current and prospective customer to contact Staraid.

The project can be viewed [at the Heroku hosted site](https://staraid-ecommerce.herokuapp.com/).

## Specification / Design

The e commerce websit for staraid will focus on the main product which is the autoguider with a few addons that you can buy for the telescope setup.   The website main function is to have a meduim to place a order and settle the payment.
A potential shopper can brows the web store to get information about the product and and create a shopping chart  (information would be like question and awnser and or the videos and reviews on the web site).
When the customer has made his d to buy the products he will need to sign in and create a profile to proceed with the order.  After registering he can proceed to choose the metohod of shipment which will add an extra amount to the total.
Then the customer can proceed the to the payment type (which for this website will be a credit card).
After the payment have been successful the customer will receive and invoice as a mail.(for future implementation)

The customer can use his profile to review and comment and rate the product.  (For the future I want a blog available where the customer can share his/her experience tell about his setup and condition and place a photo).
The home page will have a carousel where you can get a overview of picture and features,  a on offer area and an a featured product area with review will be be available.  Also review on the on offer product will be availble on the landing page.
Prospective customer can contact us via form (I will be looking at a chatbot for the future and  for customer who have order the product need to loging that we have there product availble and can be of better assistance
as for some instances they will need to add a error log).

The design of the website can been seen in more detail in the sitemap in mokups, but we will use a mostly white back ground with a bar of purple and blue sumulatin twilight. I will be using a bootstrap standard template.

In adding extra value added functionality in the future, I will be looking at tool and Api that can give weather pattern to when it will be a clear night for astrofotograpy also maybe adding best spot for astrofototographer.
 
## UX
 
### Build Data E-commerce-website-Staraid

The E-commerce-website-Staraid has the following requirements

Their primary target audiences profesional, hobbiest and starting astrofototographers
The website need to include the following 
- Database with product, prices, stock, customer, photo's and review (see detailed database digram)
- Ability to add new product to your shopping chart
- The ability to change existing shopping chart
- The ability to delete shopping chart
- View products
- Search for products
- View infromation ex Q&A, review 
- Browse the website with out signing in 
- Only user signed in can place order write a review and blog.(blogs are for future implementation)
- Register user: ability to change, (delete reviews and blogs is for future implementation)
- Fotos and videos as as infromation on the product 
- Have terms, conditions and policies 

I need the following for the website
- logo/ Name
- Data Base for product, prices, stock, review, b
- Picture, videos
- Bootstrap template
- Stripe setup
-

### Stakeholders

The following stakeholders wil interact with the website:

* Customer
* Content Manager
* Accounting (future implementation)
* Fullfillment specialist (future implementation)
* Logistics

### User stories

#### View products

As a customer I would like to view a list of products so I can select some to purchase

Acceptance criteria:

* Can see an thumbnail image for each product
* Can click to view the details of the product
* Can add to cart from details page
* Can search for a product


#### Review a product

As a customer I would like to review a product so that I can share my experience

Acceptance criteria:

* Cannot review a product if not logged in
* Can click to add a review from the product details page
* Can select a rating from the review page
* Can enter a description of my experience
* Can submit my review
* Can update my review (future implementation)
* Can delete my review (future implementation)

#### Change Shopping chart

As a customer I want the ability to review my shopping chart to make changes to it

Acceptance criteria:

* View quantities and item in the chart
* See a total cost before tax and shipping
* Remove items
* Adjust quantities of items
* Click to navigate to an item detail page

#### Check out items

As a Customer I want to check out to get my products ship to me

Acceptance criteria:

* Trigger checkout from any page if there are items in the chart
* Need to sign in
* If not registered need to register a profile (to get shipping and payment details)
* Show total include tax and shipping before finalising 
* Show confrormation messages after finalising.(future implementation)
* Verify payment vai payment processor (future implementation)

#### Register

As a customer i want to register in order to review and order products.

Acceptance criteria:

* Create a profile with full name, email, phone number, physical address and birthdate
* Trigger register when checking out
* Give and option to sign in or register
* Show on the navbar that you are signed in
* Give option in the navbar to sign out

#### View my orders (future implementation)

As a customer I want to review my orders so I can see my order history

Acceptance criteria:

* View a list of open and completed orders
* See the status of the order
* Navigate to details of the order
* Include a tracking nr if the order is shiped but not delivered
* Contact customer service from the order detail page

#### Update Product

As a content manager  I want to updated the products so I can adjust our offering over time

Acceptance criteria:

* Add and remove products
* Modify product images

####  Order report (future implementation)

As a fullfilment officer I want to print a order report  prepare the order confirm the tracking nr back

Acceptance criteria:

* Print a report for all open orders
* Updating order with the tracking nr from the transporter

#### Order Analytcs (future implementation)

As Account I want to see the order analitics and the revenue that I can track it against our goals.

Acceptance criteria:

* View dashboards with total order order and euro count
* Adjust the range with options today, this month, last 30 days, last 90 days, a year
* See chart comparing order revenu with total cost per product

#### Stock update

As a logistics officer I want to have an overview/update on the stock levels

Acceptance criteria:

* Updated the stock levels of product
* View a list of backorders (future implementation)
* View a dashboard that give the stock level and the replenishment times (future implementation)

#### Customer support

As a customer I want to contact the supplier to get information or help

Acceptance criteria:

* Complete a E-mail form

#### Writing a review

As a customer I want to write a review or rate my experience with start aid

Acceptance criteria:

* Loging as a customer
* Give a rating out of 5 (stars)
* Sudmid the written review
* Change the review (future implementation)
* Delete the review (future implementation)

#### Blog (future implementation)

As a customer I want to write a blog about astrofotograpy and how staraid has improved my experience

Acceptance criteria:

* Loging as a customer
* Post the text
* Add photo's
* Change blog
* Delete the blog
* Geo tag setup
* And select from a list telescope setup

#### Profile (future implementation)

As a customer I want to have insight in to mystarid profile to update and see software updates

Acceptance criteria:

* Update full name, email, phone number, physical address and birthdate
* View order history
* View new sofware updates available
* View your blog and reviews
* See foto's placed

#### News letter

As a customer or potential customer I want to subscribe to a newsletter

Acceptance criteria:

* Sign up for news letter
* Stop receiving newsletter


## Project Purpose

I am creating a website aimed towards current and prospective astrofototographers in search of a multifuctional easy to use autoguider for their telescope setup. 
The website will be for the primary purpose to sell the product and secondary to support and nice to have the blog and extra user information.  
The website wil be to guide the potential buyer in to buying the the product by giving enough information an the ability for extra equiry.
As a bussiness owner this website will be use to support current customer and to keep contact with them, the reason to get infromation to inprove the product and user experience.
For the businnes this website will be of value as it is our cashregister for receiving money, keeping track of stock and issuing invoices
  
### Scope of website
- A Responsive website (mobile and desktop)
- Landing page wiht product introduction and reviews
- Product view page with detail infromation
- Product search fuctionality
- Logon ability for a user
- Chart functionality
- Check out functionality which include payment and shipment
- Review functionality
- Blog post (for the future)
- Customer profile
- Order overview for Customer service
- Stock overview for Logistics
- Customer comunication via email or user account


### Website Structure

#### Database desig for e-commerce website

![Database](/doc/staraid_db_webpage.png)

#### Site Map for e-commerce website

![Site Map](/doc/sitemap_staraid_new.png)                

### Mock-up’s

In the links below you can see the mock-up’s that I drew using the mock-up tool “Pencil”:
- Desk Top

![Desk top mock-up](/doc/Start_aid_whireframe_desk.png)

- Mobile

![Mobile mock-up](/doc/Start_aid_whireframe_mobile.png)
- 
**Note that the final design has changed from the original design in the mock-ups. The reason why it has changed. I was trying different layouts while I was experimenting and learning the code and sometimes the new designs looked better than the original ones or was just more responsive. *
 
### Design Ideas

- Navbar
Standard on all the pages there will be a Navbar.  The Navbar will navigate to all sites on the website and  to Home, and have the register functionality

- The landing page 
Will have a banner with features of the main product on it.   A offer eara wher there will be the oppurtunity to go directly to the staraid main product.
A featured product area  where some product will be featured.   And the last will be some comment and review preasent on the landing page.

- Single plant view
Will have a picture, a plant table and the information on the plant.  A floating button will be available when you are loged in to change or delete the record.

- Add Plant/Crops
page will be a form where you can create the date.  The table will be updated using a checkbox.  and there will be a submit button.

- Edit, Delete and view Plant/Crops
page will be a form where you can update the date (change or delete.  The table will be updated using a checkbox.  button for delete and change with a modal.

- Search result page
This page will sow the result of the search of the name crops or nots.

- Plant Calendar
From the Navbar you can navigate here.  A table will be on this page

- Register page
Page will have a form and a submit button

- Footer
Standard on all the pages there will be a footer.


##### Font
Google fount Roboto is used

##### Colour Scheme
Green Orange and White Scheme with a purple Jumbotron

## Features

### Existing Features

The website  html pages extend from the base.html page where the navbar and footer is preasent the content displays on each page by {% block content %} and {% endblock %} tags.:

- Navbar: Every page features the navbar which signals where users can find each page. The navbar hosts the following links: Home, Shop, My Stariad, About, Contact, Search, Cart, Register and Login. The navbar is responsive and the links collapse on smaller screens, and are replaced by a hamburger menu icon.

- Footer: In this section, the user will find additional pages that can be accessed by clicking the links. It also includes the logo payment and shipping term, warranty, and policy,  and a obtion to subscribe to updates.


### Features Left to Implement

- Want to make different data object with set fields that you can choose from example pest type, soil types.
- Want to make it more sociable add a blog where user can discuss different topics regards to gardening
- Proper, secure user registration and authorisation.
- Augmenting the styling and visual effect and improved content.
- I have lose properties like soil, position, pest that i can use later to put into dashboard to make the data more visual
- A option to create your own account select your plants and get your own calendar


## Technologies Used

- Python
- HTML5
- CSS / Bootstrap 4
- CSS / Materialize
- JS / JQuery
- Mongo
- Flask
- Heroku
- Google fonts
- C9 IDE
- Google Chrome developer


## Testing

### Account App  the follwing test has been done and have pased
- Views
    - Test Login
        test_view_url_exists_at_desired_location
        test_view_uses_correct_template
        test_post_login_user
        test_post_login_invalid_user
    -Test Register
        test_view_url_exists_at_desired_location
        test_view_uses_correct_template
        test_post_creates_user
        test_post_user_form_not_valid
        test_post_profile_form_not_valid
    -Test Logout
        test_logout
     -Test Update
        test_view_url_exists_at_desired_location
        test_not_logged_in_redirects_to_login
        test_view_uses_correct_template
        test_post_update_user
        test_post_update_userform_not_valid
- Models
    -Test Profile
        test all labels model
- Backends
    -Test Case Insensitive Auth
        test_authenticate_username_good_password
        test_authenticate_email_good_password
        test_authenticate_fails_bad_password
        test_authenticate_fails_non_existent_user
        test_get_user
        test_get_user_fails_for_missing_user
- Forms
    -Test User Login Form
        test_username_or_email_label
        test_password_label
    -Test User Registration Form
        test_username_label
        test_email_label
        test_password1_label
        test_password2_label
        test_clean_email
        test_clean_email_not_unique
        test_clean_password2
        test_clean_password2_empty
        test_clean_password2_mismatch
    -Test Profile Form
        test_full_name_label
        test_birthdate_label
        test_phone_number_label
        test_country_label
        test_postcode_label
        test_town_or_city_label
        test_street_address1_label
        test_street_address2_label
    -Test User Update Forms
        test_username_label
        test_email_label

It has been tested with  Chrome Dev Tools and on my Android phone. 

Test CSS with css-validator

Test HTML with validator.w3

## Deployment

The app is deployed to Heroku and can be accessed at [].

Version control is implemented in git, by pushing the project directory to Github at [https://github.com/Lemoenskil/Milestone_project_3_Garden_planner], as well as pushing to Heroku.   
I have largely used  with detailed commit messages, to trace back changes, 
       
The database is hosted at MongoDB Atlas.
The details of the database connection are found inside the requirements.txt - it uses the os class environ method to point Heroku to its own config variable (MONGOBD_URI) in order to keep the production database connection string secret.
A Procfile is used to help Heroku to identifies them commands that are run by the application's dynos and how to run pieces of the app including the starting point app.py

## Credits

### Photos used:
Pictures used, Two gardener steampunk toys with a strawberry bush grown in a flower pot, Purchase code: 6420eb4f-b12f-48f9-842e-71d16f4bb7a5
Link to plant pictures are random an my be protected but it was tried to avoided

### Content     

 

### Work based on other code
-codepen.io for the search bar                              

### Acknowledgements

Thanks to my husband for help me test and the many hours of patience
Also, thanks to my mentor Spencer helping to clean my code and introducing me to Flask forms to sort out the user login issues.
Thanks to stack overflow without it this would not have been possible where I have used a lot of examples.
        