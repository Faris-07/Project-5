# Lowkey Menswear

This is a full-stack e-commerce project built using Django, Python, HTML, CSS and JavaScript.

Lowkey Menswear is a London based online apparel store which specialize in quality, hard-wearing clothing for an affordable price. 

The live link can be found here - [Lowkey Menswear](https://lowkey-menswear.herokuapp.com/)

![responsive](/static/images/)

# User Experience (UX)

Lowkey Menswear is a website for people aged between 18-35 to buy good quality essentials, basic's and statements pieces.

The target audience for 'Lowkey' are:
- 18 to 35 year olds
- People looking to avoid 'fast fashion'
- People looking for quality clothing

# User Stories 

#### EPIC | Navigation
- As a User I can navigate around the site so that I can easily view desired content.
- As a User, I can view a list of products so that I can choose what products to purchase.
- As a User, I can click on a product to see its details so that I can view the description, price etc.
- As a user, I can easily identify different product categories so that I can quickly view the type of products I'm looking for.
- As a User I can search for products so that I can find specific products.
- As a User, I can sort the products so that I can easily find products based on price, category, or title.
- As a User I can add items to my Wishlist so that I can save them for later.

#### EPIC | Accounts
- As a User, I can register for an account so that I can use the features given to members.
- As a User, I can receive a confirmation email when creating an account so that I know the registration was successful.
- As a User I can log in and out of my account so that I can control and manage my account
- As a User, I can recover my password in case I forget it so that I can regain access to my account.
- As a User, I can view my previous orders so that I can keep a record of what purchases I've made.
- As a User, I can save my delivery information so that I do not have to refill it out for future orders.

#### EPIC | Admin
- As an Admin, I can add products so that I can update the site's inventory.
- As an Admin, I can edit a product so that I can keep the products information up to date.
- As an Admin, I can delete a product so that I can remove products no longer available.
- As an admin, I can add coupon codes so that I can offer discounts to my customers.

#### EPIC | Purchasing
- As a User, I can add items to my basket in varying quantities so that I can keep the items in my basket until I'm ready to buy.
- As a User, I can view my bag so that I can see the total cost of the transaction and the items I will be purchasing.
- As a User, I can always see a running subtotal so that I know how much I'm spending.
- As a User, I can easily enter my payment details so that I can checkout quickly with no problems.
- As a User, I can view confirmation of my purchases so that I know the order was received and can review what I've purchased.
- As a User I can apply promotional codes so that I can receive a discount on my purchase.

#### EPIC | Interaction
- As a User I can add items to my Wishlist so that I can save them for later.
- As a User I can sign up for a newsletter to receive up to date information regarding items for sale and discounts.
- As a User, I can connect to the site's social media pages so that I can follow them and keep up to date with their products and promotions.
- As a User, I can contact the business so that I can find out any information that I require.

#### EPIC | Marketing
- As an Admin I conducted research and implemented SEO keywords to increase traffic to my website.
- As an Admin I have created a Facebook shop page to increase traffic to my website.

# Scope

In order to achieve the desired user & business goals, the following features will be included in this release:

- Responsive navbar that will navigate to the various pages throughout the site
- Landing page with image carousel with information to be found on the website
- Shop page, that displays all products available for purchase with the option to filter on the product category and price.
- My Account page, for logged in users to update their details which in turn updates the user model. User is also able to view their previous orders and wishlist.
- Register/login feature using Django AllAuth so that users can create an account.
- Custom 404 error page.

# Design

The design of the app is based on the wireframes with a mix of another clothing brand store called [COS](https://www.cos.com/en_gbp/index.html).   

## Colour Scheme
- The colour scheme for Lowkey is fairly simple, minimal and aesthetically pleasing. I used a light grey, white and some hints of black such as the black buttons to contrast the light colours of the site. I went for this style as it is clean but also because it is versatile as it matches with most colours which is important as the site would complement the colours of the product images, and keep the clothing the center of attention.

- The light grey and black are from the bootstrap light and dark classes.

## Typography
- The font used on Lowkey is Noto Sans as it is a clear and easily readable font. It is also a sleek and elegant font which goes with the theme of the site.  

## Imagery
- All the images are based on clothing and where taken from [COS](https://www.cos.com/en_gbp/index.html) and [Blacksmith-store](https://www.blacksmith-store.com/).

# Database Schema 

The design of the database can be seen below.

![Database Schema](/static/images/)

### Products

This app controls the products that are displayed in the online shop. I have created two models to store the necessary data: `Products` & `Category`.

`Products` enables individual products to be added to the database in order for them to be purchased via the online shop. Only admin users are able to access this functionality and it can be done from the front end using the `add_product` view. The admin can also edit and delete products from the front end using the `edit_product` and `delete_product` views respectively. The products model also contains the `likes` field which stores the like of a user and displays it as a wishlist item in their profile. 

This model has one Foreign Key which relates to the second model in this app, the category.

`Category` stores the various category types of the clothing on sale, this allows the user to shop by category if they are looking for something specific.

### Checkout

The checkout app is used solely for the user to make purchases via the online shop; this app contains two models, `Order` & `OrderItem`. 

`OrderItem` contains all of the information regarding the products that have been purchased as part of a specific order. It has a foreign key to `Product` & `Order`, it also contains the quantity purchased of that product and then the item total. This information is used to calculate the total cost for the order.

`Order` contains all of the relevant address information for billing/shipping, a foreign key to the `UserProfile`, email & phone number. It also contains information regarding the payment itself, the stripe PID, original basket contents (so that if the order is changed, the admin user can see what was purchased initially). Each order has an order number which is automatically generated when a new order is added to the database using `UUID`.

There are some other model methods used at various points, `update_total` calculates the overall total including any coupons that have been used depending on the order items linked to the order, ensuring the value is always correct.

### Profile

The profile app enables authenticated users to save their information so that when they are logged in the order form is pre-filled, creating an improved user experience. The `UserProfile` model is linked to the Django AllAuth user account.

# Marketing

### Plan

The Lowkey menswear website is a business to customer e-commerce platform, built and designed to sell products to the user.

To further enhance sales there is also a Lowkey menswear Facebook page, that will display information about new product arrivals and styling tips/trends. The links to the facbook page and other social sites can be found in the footer.

<i>*Note, this link may be broken as facebook regularly deletes inactive business pages.</i>

Lowkey Menswear [Facebook Page](https://www.facebook.com/profile.php?id=100086142590661)

![](assets/images/)

Users are also able to subscribe to receive the 'Lowkey' newsletter, using the MailChimp form found in the footer. 

![](assets/images/mailchimp-form.jpg)

### Search Engine Optimization

I created a sitemap.xml and robots.txt file to help aid search engines locate the site. To keep user's information safe, any pages that could contain sensitive information has been disallowed in the robots.txt.

I conducted SEO research to decide on the keywords and phrases that would be used across the website.

The initial keywords and phrases I came up with were:

#### Short Tail Keywords
- Menswear
- Clothes
- Clothing
- Affordable menswear
- Affordable Clothing
- Quality
- Quality basics
- Quality essentials

#### Long Tail Keywords
- Affordable mens clothing
- Affordable menswear
- Quality clothing
- Wardrobe staples
- Wardrobe essentials
- Mens Basic's

These phrases where used in the metadata at the head of the page.

# Features

## Navigation Bar

- ### Links
    - The navigation bar is at the top of every page and contains the links to all the other pages.
    - The navbar is fully responsive, collapsing into a hamburger menu when the screen size is small e.g. mobile. 
    - The current page is highlighted active to the user by bolder font. 
    - The Shop link drops down into a sub-menu where the user can navigate to all products or choose from one of the four product categories.

    ![Navbar-Links](assets/images/) 

- ### Search Bar
    - The search bar is located in the middle of the navbar and can be used to search all products.
    - Using the search bar will search both the product's title and description for a match.

    ![Navbar-Search](assets/images/) 

- ### Account
    - Located on the right side of the navbar is the account Icon where the user can manage their account.
    - Clicking the account icon opens a dropdown menu with options for the user to register or sign in.
    - If a user is signed in, the dropdown options change to 'My Profile' and 'Logout'.
    - If the user signed in is a super user then a third option of 'Manage' is available. 

    ![Navbar-Account](assets/images/) 

- ### Bag Icon
    - Located on the right side of the navbar next to the accounts menu is the bag icon.
    - Once a product is added to the bag, a number displaying the total quantity of items appears, located at the top right of the bag icon.
    - Clicking the bag icon navigates the user to the shopping bag page which displays a summary of the bag where the user can edit and delete products from their bag.

    ![Navbar-Bag](assets/images/)

## Home Page
    
- ### Hero Image
    - The hero image welcomes the user and tells the user to check out the latest arrivals for the season.
    - A button labelled 'Shop Now' takes the user to the products page.
    - The image will change depending on the size of the screen.

    ![Hero-Image](assets/images/)

- ### Essentials
    - The essentials cards show the user some of the product categories they should check out.
    - Clicking on one of the cards will take the user to that specififc categories page.
    - On smaller screens the cards turn into a carousel which a user can swipe through.

    ![Essentials-cards](assets/images/)

- ### Footer 
    - The footer rests at the bottom of each page.
    - The footer is responsive and breaks up the page with a black border on the top.
    - The footer is broken up into 3 sections. The about us, quick links and the newsletter sign up.
    - The Quick Links section has links to all parts of the site as well as the privacy policy.
    - The footer also includes social media links to lowkey menswear socials so they can stay up to date with any news. The links will open to a new tab to allow easy navigation for the user.
    - The footer also contains an email address so the user can contact the store.

    ![Footer](static/images/)

## Accounts

- ### Register Page
    - The register page is used to create an account.
    - The user enters a username, email, password and a confirmation of the password.
    - Once submitting the form an authentication link will be emailed to the address the user provided. 

    ![Accounts-Register](assets/images/)

- ### Login Page
    - The login page is used to log in users with an existing account.
    - The user enters their username and password.
    - A success message will appear once a user successfully logs in.
    - A Forgot Password link is also present that enables users to recover their password.

    ![Accounts-Login](assets/images/)

- ### Log out Page
    - The log out page is used to log out users who are signed in.
    - A success message will appear once a user successfully logs out.

    ![Accounts-Logout](assets/images/)

## Profile

- ### Heading
    - The heading of the page reflects the user's username.

    ![Profiles-Heading](assets/images/)

- ### Delivery Details
    - The delivery details section stores the user's delivery address and phone number.
    - The information provided here is used to autofill the delivery address when placing an order.

    ![Profiles-Delivery](assets/images/)

- ### Order History
    - The order history section is a table that keeps a record of every order the user has placed.
    - The table displays the order number, date it was ordered, items ordered, quantities of items, size of items and the order total.
    - Hovering over the truncated order number reveals the whole order number.
    - Clicking the order number will take the user to a more detailed summary of the order.
    - The five most recent items are shown on the order history list.

    ![Profiles-Order-History](assets/images/)

- ### Wishlist
    - The wishlist section contains all the products the user has liked.

    ![Profiles-Wishlist](assets/images/)

## All Products

- ### Sorting
    - The sort-by box is located to the top right of the products section on medium and large screens, and centred on smaller screens.
    - Clicking the box opens up a dropdown menu with price options on how to sort the products e.g. Price (Low to High). 

    ![Products-sort](assets/images/)

- ### Products Page
    - The products page is fully responsive, adjusting how many products are on each row depending on the user's screen size.
    - Each product card shows an image of the product, title and price.
    - Clicking anywhere inside the product card will take the user directly to that products detail page.
    - Each product is broken down into their categories with a matching heading.

## Product Details

- ### Product Information
    - The page is split between the product image on one side and the product information on the other for larger screens, and with the image on top and information on the bottom for smaller screens
    - The product information section shows information about the product such as its name, description, size, composition, quantity and price.
    - If the user is a super user, the edit and delete buttons will appear underneath the "add to bag" button.

    ![Products-Product-Info](assets/images/)

- ### Like Button
    - The heart (like) button is located on the top right corner of the product image.
    - The heart button renders as empty if either the user is signed out or the product is not liked by the user.
    - Liking a product fills in the heart and adds the product to the user's wishlist items list on their profile page.
    - Unliking a product unfills the heart and removes the product from the user's wishlist items list on their profile page.
    - If the heart is clicked when a user is not signed in, an 'Account Required' modal pops up informing the user that they need to either sign in or create an account to use that feature.
     
    ![Products-Like](assets/images/)

- ### Quantity Buttons
    - The quantity buttons are located underneath the product composition and are used to add a chosen amount of the item to the bag.
    - The up arrow and down arrow buttons increase and decrease the input value. 
    - If the value is set to 1 the minus quantity will be disabled. Respectively if the value is set to 5 the plus button is disabled.
    - Clicking the 'Add to Bag' button takes the number in the input field and adds that amount of products to the bag.
    - Clicking the 'Add to Bag' button when the input is blank adds one item to the bag.
    - Trying to add an amount less than 1 or above 5, renders an error message informing the user of the parameters needed to add an item to their bag.

    ![Products-Quantity-Button](assets/images/)

## Bag

- ### Items
    - The bag page displays all items that the user has added to it. 
    - The page will list the items added with its image, followed by its title and SKU. 

    ![Bag-Items](assets/images/)

- ### Quantity and Price
    - The price and quantity section has four elements, the product's price, size, quantity, and the subtotal of that item's line.
    - The quantity element has buttons either side for the user to increase or decrease the total of that item in the bag.
    - The minus quantity button will be disabled if the quantity of the item is one. The plus button will also be disabled if the quantity of the item is 5.
    - Under the quantity selector is the update and delete buttons.
    - Clicking the 'Update' button saves any changes to the quantity and updates the item's subtotal which in turn updates the order total.
    - Clicking the 'Remove' button removes the item completely from the user's bag. 
    - Manually inputting the number zero or anything below and clicking 'Update' will remove the item from the bag. 
    - Manually inputting a number above 5 and clicking 'update' will result in an error message informing the user of the correct parameters. 
    
    ![](assets/images/)
    
- ### Totals and messaging
    - At the end of the order items is a summary of the costs.
    - The summary features the bags subtotal, delivery charges and the total to pay.
    - Under the order total is two buttons. Where the user can either continue to the checkout or return to the products page by clicking 'Continue Shopping' which turns into 'Back' on smaller screen sizes.

    ![](assets/images/)

- ### Coupons
    - Above the subtotal is an input box where users can enter a coupon code.
    - If the coupon code entered is valid, a success message will be displayed and a summary of the coupon added, and the discount given will be shown above the delivery and order totals.
    - If the coupon code entered is invalid, an error message will be displayed, and the totals will not change.

    ![Bag-Coupons](assets/images/)

## Checkout

- ### Details
    - The details section appears on the left on large screens or underneath the order summary on smaller screens.
    - The user fills out their contact details, delivery address, and card number.
    - If the user is a guest user, a link to create an account or login is displayed under the delivery information form.
    - If the user is signed in a checkbox to save the delivery information can be checked.
    - If the user is signed in and has delivery information saved, the delivery details and email address will be automatically filled in. 
    - All fields that have an Asterix are required. If any field is left blank on the form then the affected field will be highlighted.  

    ![Checkout-Details](assets/images/)

- ### Order Summary
    - The order summary section appears on the right on large screens or at the top on smaller screens. 
    - This section lists all the items about to be purchased, along with the quantity, size, subtotal, delivery and order total.
    - Clicking the image of any items in the summary will take the user to that specific product's detail page. 

    ![Checkout-Order-Summary](assets/images/)

- ### Payment
    - Underneath the delivery details is the card payment box which is from [Stripe](https://dashboard.stripe.com/login). 
    - Only numbers can be entered into the card payment box. Incorrect card numbers will automatically show an invalid card number error.
    - The site can be tested by using the Stripe dummy card number 4242 4242 4242 4242 with the expiry date 04/24 and the CVC code 242.
    - At the bottom of the page there is the 'Complete order' and 'Bag' button which either let the user checkout or return back to their bag. There is also a warning message informing the user of how much their card is about to be charged.

    ![Checkout-Payment](assets/images/)


- ### Loading Spinner
    - When the form is valid and the user makes the payment a loading spinner will render until the information is processed. 
    
    ![Checkout-Spinner](assets/images/)

- ### Confirmation 
    - Once the order has been processed the user is taken to the checkout success page.
    - This page summarises the completed order. It lists the order number, order date, the items ordered with their quantities, item images, delivery address, and the billing info. 
    - A confirmation email is sent to the email address provided, and this is displayed at the top of the page. 
    - At the end of the summary is a button that the user can click which will take them back to the main shop.
    
     ![Checkout-Confirmation](assets/images/)

## Product Management - Admin

- ### Add Product
    - The add product page is accessed by the account dropdown menu, under "Manage". It is only accessible by superusers/admin.
    - The form lists all the required fields to create a new product. 
    - The user must fill out all the fields that contain an Asterix. Failure to do so will display an error message containing which fields are missing.
    - The SKU field must be unique. An error message will appear if the user inputs an SKU that already exists.
    - If a price is added with more than 6 digits the form will fail and an error message will appear under the price field.
    - The user has the option to add an image. If none is chosen then a default image is used.
    - Clicking the 'Add Product' button at the bottom of the form will create the product if the form is valid.

    ![Product-Management-Add](assets/images/)

- ### Edit Product
    - The edit product page can only be accessed by superusers/admin. 
    - The edit product page can be accessed by clicking the edit button located under the 'add to bag' on the products detail page.
    - The edit product page is identical to the add product page but allows superusers to edit the selected product. The details of the product is already filled in. 
    - The image field displays a thumbnail of the current image and has a checkbox option to remove it. Checking this will change the image to the default image.
    - Clicking the 'Update Product' button will save any changes made to the existing product.  

    ![Product-Management-Edit](assets/images/)

- ### Delete Product
    - Only superusers can delete products.
    - The Delete Product button can be found to the left of the 'edit' button on the products detail page. 
    - Clicking the delete button will bring up a delete confirmation modal, asking the user if they are sure they want to delete the product, and informing them that it can not be undone. 
    - Once the warning modal has been activated, if the user then clicks the delete button the product will be deleted from the database. 
    - If the user decides they do not want to delete the product they can press the cancel button or click outside of the modal. The modal will close and there will be no effect to the product and database. 

    ![Product-Management-Delete](assets/images/product-management-delete.png)

## More Features

- ### Back To Top Button
    - On large screens, once the user has scrolled past a certain point on the page, a button will appear at the bottom right of the screen.
    - The button has a fade in and fade out animation to make it feel smoother and effortless adding to the user experience.
    - Clicking the button scrolls the user back to the top of the page. 

    ![Scroll-arrow](assets/images/)

- ### 404 page
    - If any links are broken or the user types in an address that doesn't exist, a custom 404 error page will be rendered.

    ![404](assets/images/)

- ### Responsiveness 
    - Every page on this site is fully responsive. This allows for a smoother overall experience no matter the size of the device, therefore improving the user experience.

## Features left to implement
*There are no features left to implement from the initial scope of my project, however I have some features that I would like to add in the future.*

- A FAQ page helping users with commonly asked questions.
- A top products feature to dynamically show the top/bestselling products.
- Option to share products on social media.

## Technologies

### Languages used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

### Libraries and Programs Used

- [Git](https://git-scm.com/)
    - Version control.
- [GitHub](https://github.com/)
    - For storing code and deploying the site.
- [Gitpod](https://www.gitpod.io/)
    - Used for building and editing my code.
- [Django](https://www.djangoproject.com/)
    - A python based framework that was used to develop the site.
- [Bootstrap](https://getbootstrap.com/)
    - For help designing the html templates.
- [Google Fonts](https://fonts.google.com/)
    - Used to style the website's logo.
- [Font Awesome](https://fontawesome.com/)
    - Used to obtain the icons used.
- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    - Used to help fix problem areas and identify bugs.
- [AWS](https://aws.amazon.com/)
    - Used to store static files and images.
- [Favicon.io](https://favicon.io/)
    - Used to generate the site's favicon.
- [DrawSQL](https://drawsql.app/)
    - Used for ERD diagram.
- [PostgreSQL](https://www.postgresql.org/)
    - Database used through heroku.
- [W3C Markup Validation Service](https://validator.w3.org/) 
    - Used to validate HTML code.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Used to validate CSS code.
- [Pep8](http://pep8online.com/)
    - Used to validate Python code.
- [JSHint](https://jshint.com/)
    - Used to validate JS code.
- [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - Used to render forms.
- [Django-tempus-dominus](https://pypi.org/project/django-tempus-dominus/)
    - Used for a date and time picker on add coupon page.
- [Stripe](https://stripe.com/en-gb)
    - Used to take payments and generate webhooks.
- [Heroku](https://www.heroku.com/)
    - To deploy the project.