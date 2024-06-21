# THE POKÉMON WEBSITE 
#### Description:

This is The Pokémon Website. So i started this project started as an idea from Week 0 when i learned to work with Scratch. I am a huge Pokemon fan, and the series is ended so i thought to give a tribute and also i wanted to understand how the Pokemon Website works behind the screen, so i created a One!. Okay so first comes first our

1. ** models.py ** - It contains User model for the User who has signed in or out, Category Model in which Pokemons can be grouped according to their categories , Bid model in which a user can buy things but i have not used it in my website as a Bid or Buying, Listing Model for the data of Pokemon about its Name, Description Pokemon Number , Comment Model that represents comment made on Pokemon by User and Lastly Post Model for Post/ Forums.

2. ** views.py ** - It handles user interactions and requests, supporting various functionalities such as user authentication, listing management, bidding, commenting, and post creation. User Authentication: Login Authenticates users and logs them in, Logout : Logs users out, Register : Registers new users, handling user creation and validation. Post Management: Forum : Displays all posts on the forum. Create Post : Handles the creation of new posts via a form. Static Pages: Story , Animation. Listings - Index : Displays Pokemons with pagination and categories, Listing Detail : Shows details of a specific pokemon, including comments and owner information. Create Listing : Allows users to add new Pokemon with details like title, description, URL, category, and pokemon number. Add and Remove from Watchlist are not in using i thought of Using them for Adding Pokemons to the Team but changed the decision.  Close Auction and Add Bid are also not in use i thought of making a Pokemon Mart Section where Users can buy Potion and Pokeball but again decided not to implement this function  Add Comment : It Enables users to add comments to a Pokemon. Display Listings by Category : It filters and displays pokemons by selected category.

3. ** urls.py ** - It conatins the path of the funcitons.

4. ** templates ** - This is the Main Part of this Website. **I have written All the javascript functions in the respective HTML where it was needed. **  

    1. Story.html - It has all the main content of the Story section. I have tried to make this page look exact as the original Pokemon website using Html and Css. For Javascript Functionality it conatins :- Image Slider: It  Controls the image slider’s navigation through nextSlide and prevSlide functions. Scroll to Top: Displays a button to scroll back to the top of the page when the user scrolls down. it won't show if the user is at the top of Page.

    2. Login.html and Register.html :- They are pretty same as User can Login and register throgh this Section.

    3. Index.html - This is the Main File as all the Pokemon details appear in this page. IT's layout and style is also pretty much same as the orginal Pokemon Website. Every Pokemon details appear on this page we can look the details of a specific pokemon by clicking their name. This page also contains several functions Search Function by using javascript function , if a user search any pokemon name or its number that pokemon will be displayed on the page and also related search will also show on the page. Surprise Me Button: By pressing this button it scrolls to a random set of Pokemons. Sort By Function by choosing a specific category all the pokemons related to that category will show on the page.

    4. Create.html :- In this page an user can add any New Pokemon he discovers which is not in the Pokedex. the user will have to add the Pokemon Name, description, url link for the image of pokemon, pokemon number and Have to choose the category for the Pokemon.

    5. Forum.html :- Scroll to Top Button: Functions to display the button when scrolling and to implement smooth scrolling behavior. Comment Seciton: An interactive comment section where users can post and edit comments. The comments are displayed with the poster's name, date, and time.

    6. Listing.html :- It contains all the details of the Pokemon and the comment section where any user can comment their thoughts about the Pokemon or ask any doubt related to that Pokemon. 

    7. Watchlist.html :- It was meant to add pokemon to the team of user but it is not in use.

    8. Layout.html :- It contains the layout of all the Pages.

    9. Animation.html :- This html has been added just for entertainment.

Lastly!! I'm so grateful for CS50 and Brian for teaching me how I can make it happen with code!

This Was CS50W!!!