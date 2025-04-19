import streamlit as st
import pandas as pd

st.set_page_config(page_title="Book Log", layout="centered", initial_sidebar_state="expanded", page_icon="📚")

# Initialize session state
if 'library' not in st.session_state:
    st.session_state.library = pd.DataFrame(columns=[
        "ISBN", "Title", "Author", "Year", "Genre", "Total Copies", "Borrowed", "Available"
    ])

# Genre list
genres = [
    "Fantasy", "Mystery", "Thriller / Suspense", "Horror", "Romance", "Adventure", "Drama",
    "Children’s Fiction", "Satire", "Biography", "History", "Science & Technology", "Philosophy",
    "Religion & Spirituality", "Politics & Current Affairs", "Business & Economics", "Health & Wellness",
    "Travel", "Education", "Art & Photography", "Cookbooks / Food","Ghazal", "Nazm", "Dastan", 
    "Drama (Urdu Theatre)","Folk Literature", "Travel Writing"
]

# Author suggestions
authors = [
    # Classic Authors
    "William Shakespeare", "Charles Dickens", "Jane Austen", "George Orwell", "Thomas Hardy",
    "Emily Brontë", "Charlotte Brontë", "Mary Shelley", "Lewis Carroll", "Oscar Wilde",
    "H.G. Wells", "Rudyard Kipling", "Arthur Conan Doyle", "Virginia Woolf", "E.M. Forster",
    "Joseph Conrad", "D.H. Lawrence", "Robert Louis Stevenson", "John Milton", "William Blake",
    "Samuel Taylor Coleridge", "Percy Bysshe Shelley", "Alfred Lord Tennyson", "Elizabeth Gaskell", "Daniel Defoe",

    # Mystery / Detective
    "Agatha Christie", "Dorothy L. Sayers", "P.D. James", "Ruth Rendell", "Colin Dexter",
    "Ian Rankin", "Ellis Peters", "Minette Walters", "Peter James", "Ann Cleeves",

    # Modern / Contemporary Fiction
    "Ian McEwan", "Zadie Smith", "Julian Barnes", "Hilary Mantel", "Salman Rushdie",
    "Kazuo Ishiguro", "Martin Amis", "Nick Hornby", "Jeanette Winterson", "David Nicholls",
    "Jojo Moyes", "Maggie O’Farrell", "David Mitchell", "Matt Haig", "Rachel Cusk",

    # Fantasy / Sci-Fi
    "J.K. Rowling", "J.R.R. Tolkien", "C.S. Lewis", "Terry Pratchett", "Neil Gaiman",
    "Philip Pullman", "Douglas Adams", "Susanna Clarke", "China Miéville", "Joe Abercrombie",

    # Young Adult / Children’s
    "Roald Dahl", "Enid Blyton", "Jacqueline Wilson", "Michael Morpurgo", "Julia Donaldson",
    "Anthony Horowitz", "Malorie Blackman", "Eoin Colfer", "Frances Hodgson Burnett", "Kenneth Grahame",

    # Poets & Playwrights
    "T.S. Eliot", "W.H. Auden", "Seamus Heaney", "Ted Hughes", "Carol Ann Duffy",
    "Philip Larkin", "Dylan Thomas", "John Keats", "Lord Byron", "Andrew Marvell",

    # Non-Fiction / Philosophy / Essays
    "Bertrand Russell", "George Bernard Shaw", "Christopher Hitchens", "Richard Dawkins", "Stephen Hawking",
    "Mary Beard", "Simon Schama", "A.N. Wilson", "Alain de Botton", "Niall Ferguson",

    # Others / Popular
    "William Golding", "John le Carré", "E.L. James", "Paula Hawkins", "Sarah Waters",
    "Sophie Kinsella", "Ben Okri", "Hanif Kureishi", "William Boyd", "Amanda Craig"
    "George Orwell", "Jane Austen", "J.K. Rowling", "Agatha Christie", "Ernest Hemingway",
    "Toni Morrison", "Stephen King", "Chimamanda Ngozi Adichie", "Haruki Murakami",
    "Khaled Hosseini", "Isabel Allende", "Colleen Hoover", "Taylor Jenkins Reid",
    "Brandon Sanderson", "Emily Henry", "Ali Smith", "Elif Shafak", "Kazuo Ishiguro",
    "S.M. Abdullah Abdulbadeeii", "Syed Serajuddin Seraj", "Umaima Kazi",

    # Classical Poets & Writers
    "Mirza Ghalib", "Allama Iqbal", "Mir Taqi Mir", "Sir Syed Ahmed Khan", "Maulana Hali",
    "Shibli Nomani", "Mohammad Hussain Azad", "Maulana Abul Kalam Azad", "Josh Malihabadi", "Hasrat Mohani",

    # Progressive Writers
    "Saadat Hasan Manto", "Ismat Chughtai", "Krishan Chander", "Rajinder Singh Bedi", "Faiz Ahmed Faiz",
    "Ali Sardar Jafri", "Majaz Lakhnawi", "Ahmed Nadeem Qasmi", "Habib Jalib", "Jan Nisar Akhtar",

    # Modern Fiction & Literature
    "Intizar Hussain", "Qurratulain Hyder", "Bano Qudsia", "Ashfaq Ahmed", "Mumtaz Mufti",
    "Ibn-e-Insha", "Shaukat Siddiqui", "Anwar Maqsood", "Mustansar Hussain Tarar", "Umera Ahmed",
    
    # Religious & Philosophical
    "Maulana Maududi", "Maulana Ashraf Ali Thanvi", "Allama Shibli Nomani", "Maulana Wahiduddin Khan", "Maulana Tariq Jamil",
    "Mufti Taqi Usmani", "Mufti Muhammad Shafi", "Dr. Israr Ahmed", "Maulana Yousuf Ludhianvi",

    # Poets (Classical to Modern)
    "Parveen Shakir", "Jaun Elia", "Nasir Kazmi", "Ahmad Faraz", "Zehra Nigah",
    "Amjad Islam Amjad", "Anwar Masood", "Kishwar Naheed", "Faraz Ahmed Faraz", "Jamiluddin Aali",

    # Humor & Satire
    "Mushtaq Ahmad Yusufi", "Ibne Insha", "Anwar Maqsood", "Omer Sharif", "Zia Mohyeddin",
    "Shafiq-ur-Rehman", "Dr. Younas Butt", "Hanif Khalid", "Aftab Iqbal", "Ali Moeen Nawazish",

    # Journalists & Columnists
    "Irfan Siddiqui", "Haroon Rasheed", "Javed Chaudhry", "Hassan Nisar", "Arshad Sharif",
    "Hamid Mir", "Ansar Abbasi", "Talat Hussain", "Orya Maqbool Jan", "Ayaz Amir",

    # Contemporary Novelists / Writers
    "Nimra Ahmed", "Farhat Ishtiaq", "Hashim Nadeem", "Aleem-ul-Haq Haqqi", "Nadia Ahmad",
    "Rahat Jabeen", "Samra Bukhari", "Seema Ghazal", "Bushra Rehman", "Faiza Iftikhar",

    # Urdu Language Contributors
    "Gopi Chand Narang", "Jameel Jalibi", "Rasheed Ahmad Siddiqui", "Farman Fatehpuri", "Moin Akhtar",
    "Anis Nagi", "Aslam Farrukhi", "Tariq Aziz", "Ashfaq Sarwar", "Zafar Iqbal",

    # Scriptwriters & Dramatists
    "Haseena Moin", "Amjad Islam Amjad", "Anwar Maqsood", "Khalil-ur-Rehman Qamar", "Sarmad Sehbai",
    "Asghar Nadeem Syed", "Munnu Bhai", "Imran Aslam", "Fatima Surayya Bajia", "Noor ul Huda Shah"
]

# Language options
languages = [
    "English", "Mandarin Chinese", "Hindi", "Spanish", "French", "Arabic", "Bengali", "Portuguese", 
    "Russian", "Urdu", "Indonesian", "Standard German", "Japanese"
]

# Helper functions
def is_duplicate_isbn(isbn):
    return isbn in st.session_state.library["ISBN"].values

def refresh_available():
    st.session_state.library["Available"] = st.session_state.library["Total Copies"] - st.session_state.library["Borrowed"]

# Sidebar navigation
st.sidebar.markdown("# 📚 Navigation")
sidebar_option = st.sidebar.radio("", ["Library Records", "About App", "About Us", "About Me" ])

if sidebar_option == "About App":

    st.title("📘 About This App")
    st.markdown("""
    ## Welcome to Your Personal Library Manager!

    This **Personal Library App** is designed to help individuals, students, librarians, and book enthusiasts to manage their book collection effortlessly. Whether you're a reader wanting to track your favorite books or a librarian managing a vast collection, this app provides all the necessary tools in one convenient platform.

    ### Key Features:
    1. **Book Record Management**:
        - Add new books with detailed information such as **ISBN**, **Title**, **Author**, **Year**, and **Genre**.
        - Edit or delete book records with ease.
        - Prevent duplicate entries with **ISBN validation**.
    
    2. **Book Borrowing & Availability Tracking**:
        - Track borrowed books and their return status.
        - Check the availability of books in real-time (e.g., whether they are currently borrowed or available).
        - Automatically update the availability of books when they are borrowed or returned.
    
    3. **Search & Filter**:
        - Easily search for books by **Title**, **Author**, or **Genre**.
        - Filter books by **Genre** or **Year** to quickly find what you are looking for.
    
    4. **Data Export**:
        - Download the entire book record in **CSV** format for further analysis or backup.
    
    5. **Language Support**:
        - The app supports a variety of languages, allowing you to choose the language of your preference (English, Mandarin Chinese, Hindi, Spanish, French, Arabic, Bengali, Portuguese, Russian, Urdu, Indonesian, Standard German, Japanese).

    ### Why Use This App?
    - **Efficient Organization**: Keep your personal or library book collection neatly organized with all relevant details in one place.
    - **Time-Saving**: No need to manually track books or borrowings—this app does it automatically.
    - **User-Friendly Interface**: The intuitive Streamlit interface ensures that users, even those with no technical background, can easily navigate the app.

    ### How It Works:
    1. **Add New Books**: Simply enter the book's ISBN, Title, Author, Genre, and Year to create a new record.
    2. **Track Borrowings**: Select a book to mark it as borrowed, and it will automatically update its availability status.
    3. **Edit & Delete Records**: If you make an error or no longer need a record, you can quickly edit or delete it.
    4. **Language Selection**: Choose your preferred language for better accessibility and comfort.
    5. **Download Data**: When you’re ready, export all book records as a CSV file to keep a backup or share with others.

    ### Technologies Used:
    - **Streamlit**: For building the interactive web interface.
    - **Pandas**: For managing book records and data manipulation.
    - **Python**: For backend logic, including book management, data validation, and more.

    ### Future Plans:
    - **Mobile Version**: To allow on-the-go management of your library.
    - **Barcode Scanning**: Integration with barcode scanners to add books more efficiently.
    - **User Authentication**: Add login functionality to personalize the app for different users.

    ### How to Contribute:
    If you want to contribute to this app, feel free to fork the repository and submit your pull requests. Your ideas, improvements, or bug fixes are always welcome!

    ### About the Developer:
    **S.M. Abdullah Abdulbadeeii** – Developer and Founder of **SMAASU City Builders**. Passionate about using technology to solve everyday problems, particularly in the fields of **civil engineering**, **data science**, and **app development**.

    Feel free to reach out to me via the [Contact](#) page for any suggestions, bug reports, or collaborations.
    """)

elif sidebar_option == "About Us":
    col1, col2, col3 = st.columns([1,8,1])
    with col2:
        st.markdown(
        "<img src='https://github.com/smaasui/SMAASU/blob/main/smaasu_corp_white.png?raw=true' width='550'>",
        unsafe_allow_html=True)

        # Company Title
        st.write("# 🏢 About SMAASU Corporation")

        # Introduction
        st.markdown(
            """
            **SMAASU Corporation** is a forward-thinking company committed to innovation in **technology, architecture, and sustainable urbanization**.
            Our vision is to create cutting-edge solutions that simplify workflows, enhance productivity, and contribute to a smarter, more efficient future.
            """
        )

        # Mission Section
        st.header("🌍 Our Mission")
        st.markdown(
            """
            At **SMAASU Corporation**, we aim to:
            - 🚀 **Develop pioneering software solutions** that enhance business efficiency.
            - 🏗️ **Revolutionize architecture and urban planning** with smart, sustainable designs.
            - 🌱 **Promote sustainability** in every project we undertake.
            - 🤝 **Empower businesses and individuals** with next-gen technology.
            """
        )

        # Core Values Section
        st.header("💡 Our Core Values")
        st.markdown(
            """
            - **Innovation** – Continuously pushing boundaries with cutting-edge technology.
            - **Sustainability** – Building a future that is eco-friendly and efficient.
            - **Excellence** – Delivering top-tier solutions with precision and quality.
            - **Integrity** – Upholding transparency and trust in every endeavor.
            """
        )

        # Call to Action
        st.markdown(
            """
            🚀 **Join us on our journey to create a smarter, more sustainable world with SMAASU Corporation!**
            """,
            unsafe_allow_html=True
        )
        st.link_button("🔗 Visit SMAASU Corporation", "https://g.co/kgs/VvQB8W9")

elif sidebar_option == "About Me":
    st.write("# 🏅 Syed Muhammad Abdullah Abdulbadeeii")
    col1, col2, col3 = st.columns([4.5,1,4.5])
    with col1:
    # Personal Title 🏅🌟💡🌱🌍👤
        st.write("\n\n")
        st.markdown(
        "<img src='https://raw.githubusercontent.com/smaasui/SMAASU/main/16.jpeg' width='550'>",
        unsafe_allow_html=True)

        # st.image("https://raw.githubusercontent.com/smaasui/SMAASU/main/16.jpeg", use_container_width=True, width=100)
        # Expertise & Interests
        st.write("\n\n")
        st.write("# 🚀 Areas of Expertise")
        st.markdown(
            """
            - 🏗️ **Civil Engineering & Smart Infrastructure** – Engineering sustainable and innovative urban solutions.
            - 💻 **Software & Web Development** – Creating intelligent digital solutions to optimize efficiency.
            - 🤖 **Artificial Intelligence & Data Science** – Harnessing AI-driven technologies for smarter decision-making.
            - 📊 **Data Processing & Automation** – Streamlining complex workflows through advanced automation.
            - 🚀 **Entrepreneurship & Technological Innovation** – Spearheading startups that drive meaningful change.
            - ❤️ **Philanthropy & Social Impact** – Advocating for and supporting communities in need.
            """
        )


    with col3:
        st.write("# 🌱 About Me")
        # Introduction
        st.markdown(
            """
            I am **Syed Muhammad Abdullah Abdulbadeeii**, a **Civil Engineering Student at NED University of Engineering & Technology, Entrepreneur, Innovator, and Philanthropist**. 
            With a deep passion for **Artificial Intelligence, Architecture, and Sustainable Urbanization**, I am committed to pioneering **Transformative Solutions** that seamlessly integrate technology with real-world applications.
            
            My work is driven by a vision to **Build a Smarter, More Sustainable Future**, where cutting-edge innovations enhance efficiency, improve urban living, and empower businesses. 
            Beyond my professional pursuits, I am dedicated to **philanthropy**, striving to **uplift Muslims and support underprivileged communities**, fostering a society rooted in compassion, empowerment, and progress.
            """
        )
        
        # Vision & Journey
        st.write("# 🌍 My Vision & Journey")
        st.markdown(
            """
            As the founder of **SMAASU Corporation**, I have led groundbreaking initiatives such as **Data Duster**, a web-based platform revolutionizing data processing and automation. 
            My entrepreneurial journey is fueled by a relentless drive to **bridge the gap between technology and urban development**, delivering impactful solutions that **redefine the future of cities and industries**.
            
            **I believe in innovation, sustainability, and the power of technology to transform lives.** Through my work, I strive to create solutions that not only drive efficiency but also foster inclusivity and social well-being.
            
            **Let’s collaborate to build a brighter, more progressive future!**
            """
        )
        
    st.write("# 🔗 Engineering connections !")
    st.link_button("🔗 Stay connected on LinkedIn!", "https://www.linkedin.com/in/smaasui/")

elif sidebar_option == "Library Records":
    st.markdown("# Book Log")

    tab1, tab2, tab3 = st.tabs(["➕ Add Record", "✏️ Edit/Delete Record", "📋 View Records"])

    # --------- ➕ ADD RECORD ---------
    with tab1:
        st.header("➕ Add New Book")
        with st.form("AddBook"):
            isbn = st.text_input("ISBN")
            title = st.text_input("Book Title")
            author = st.selectbox("Author", authors + ["Other"])
            if author == "Other":
                author = st.text_input("Enter Author Name")
            year = st.number_input("Publication Year", min_value=1000, max_value=9999, step=1)
            genre = st.selectbox("Genre", genres)
            total = st.number_input("Total Copies", min_value=1, step=1)

            submitted = st.form_submit_button("Add Book")
            if submitted:
                if not isbn.isdigit():
                    st.warning("⚠️ ISBN must contain only digits.")
                elif is_duplicate_isbn(isbn):
                    st.warning("⚠️ Book with this ISBN already exists!")
                else:
                    new_row = pd.DataFrame(
                        [[isbn, title, author, year, genre, total, 0, total]],
                        columns=st.session_state.library.columns
                    )
                    st.session_state.library = pd.concat([st.session_state.library, new_row], ignore_index=True)
                    st.success("✅ Book added!")

    # --------- ✏️ EDIT/DELETE RECORD ---------
    with tab2:
        st.header("✏️ Update / ❌ Delete Book")
        if not st.session_state.library.empty:
            selected_isbn = st.selectbox("Select a book by ISBN", st.session_state.library["ISBN"])
            book = st.session_state.library[st.session_state.library["ISBN"] == selected_isbn].iloc[0]

            new_title = st.text_input("Title", book["Title"])
            new_author = st.text_input("Author", book["Author"])
            new_year = st.number_input("Year", value=int(book["Year"]), min_value=1000, max_value=9999)
            new_genre = st.selectbox("Genre", genres, index=genres.index(book["Genre"]) if book["Genre"] in genres else 0)
            new_total = st.number_input("Total Copies", value=int(book["Total Copies"]), min_value=1)

            col1, col2 = st.columns(2)
            if col1.button("Update Book"):
                idx = st.session_state.library[st.session_state.library["ISBN"] == selected_isbn].index[0]
                st.session_state.library.at[idx, "Title"] = new_title
                st.session_state.library.at[idx, "Author"] = new_author
                st.session_state.library.at[idx, "Year"] = new_year
                st.session_state.library.at[idx, "Genre"] = new_genre
                st.session_state.library.at[idx, "Total Copies"] = new_total
                refresh_available()
                st.success("✅ Book updated!")

            if col2.button("Delete Book"):
                st.session_state.library = st.session_state.library[st.session_state.library["ISBN"] != selected_isbn]
                st.success("🗑️ Book deleted!")

    # --------- 📋 VIEW RECORDS ---------
    with tab3:
        st.header("📋 Library Records")
        st.dataframe(st.session_state.library)

