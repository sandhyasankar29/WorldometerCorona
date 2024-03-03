import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

class worldometerCoronaApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Worldometer Corona")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=50)
        self.container.grid_columnconfigure(0, weight=50)
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select the Module to execute")
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Module 3.1", command=lambda: controller.show_frame(PageOne))
        button1.pack()
        button2 = tk.Button(self, text="Module 3.2", command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Module 3.1")
        label.pack(pady=10,padx=10)

        # Section 1
        section1_label = tk.Label(self, text="Extract data", font=("Helvetica", 16, "bold"))
        section1_label.pack(pady=(10, 5))

        # Create a Combobox
        label = tk.Label(self, text="Select Country/Continent: ")
        label.pack(pady=10)

        options = ['Asia','North','Europe','South','Oceania','Africa','World','China','USA','India','France','Germany','Brazil','S._Korea','Japan','Italy','UK','Russia','Turkey','Spain','Australia','Vietnam','Taiwan','Argentina','Netherlands','Mexico','Iran','Indonesia','Poland','Colombia','Greece','Austria','Portugal','Ukraine','Chile','Malaysia','Canada','Belgium','Israel','DPRK','Thailand','Czechia','Peru','Switzerland','Philippines','South','Romania','Denmark','Singapore','Hong','Sweden','Serbia','New','Iraq','Hungary','Bangladesh','Slovakia','Georgia','Jordan','Ireland','Pakistan','Finland','Norway','Kazakhstan','Lithuania','Slovenia','Bulgaria','Croatia','Guatemala','Morocco','Lebanon','Costa','Bolivia','Tunisia','Cuba','Ecuador','UAE','Panama','Uruguay','Mongolia','Nepal','Belarus','Latvia','Saudi','Paraguay','Azerbaijan','Bahrain','Cyprus','Dominican','Sri','Kuwait','Myanmar','Moldova','Estonia','Palestine','Venezuela','Egypt','Qatar','Libya','Ethiopia','Runion','Honduras','Armenia','Bosnia','Oman','Luxembourg','North','Zambia','Kenya','Brunei','Albania','Botswana','Montenegro','Algeria','Nigeria','Zimbabwe','Uzbekistan','Mozambique','Afghanistan','Martinique','Laos','Iceland','Kyrgyzstan','Guadeloupe','El','Trinidad','Maldives','Namibia','Uganda','Ghana','Jamaica','Cambodia','Rwanda','Cameroon','Malta','Barbados','Angola','Channel','DRC','French','Malawi','Senegal','Ivory','Suriname','New','French','Eswatini','Guyana','Belize','Fiji','Madagascar','Cabo','Sudan','Mauritania','Bhutan','Syria','Burundi','Seychelles','Gabon','Andorra','Papua','Curaao','Aruba','Tanzania','Mauritius','Mayotte','Togo','Guinea','Bahamas','Isle','Lesotho','Haiti','Faeroe','Mali','Cayman','Saint','Benin','Somalia','Micronesia','San','Solomon','Congo','Macao','Timor-Leste','Burkina','Liechtenstein','Gibraltar','Grenada','Bermuda','South','Nicaragua','Tajikistan','Equatorial','Monaco','Samoa','Tonga','Marshall','Dominica','Djibouti','CAR','Gambia','Saint','Vanuatu','Greenland','Yemen','Caribbean','Sint','Eritrea','Niger','St.','Guinea-Bissau','Comoros','Antigua','Liberia','Sierra','Chad','British','Cook','Sao','Turks','Saint','Palau','St.','Nauru','Kiribati','Anguilla','Wallis','Saint','Tuvalu','Saint','Falkland','Montserrat','Niue','Diamond','Tokelau','Vatican','Western','MS']
        options.sort()
        self.selected_option = tk.StringVar(self)
        self.selected_option.set(options[0])  # Set default value
        dropdown = tk.OptionMenu(self, self.selected_option, *options)
        dropdown.pack(pady=(0, 5))

        # Execute Button
        execute_button = tk.Button(self, text="Execute", command=self.execute_program)
        execute_button.pack(pady=10)

        # Section 2
        section2_label = tk.Label(self, text="Extract percentage", font=("Helvetica", 16, "bold"))
        section2_label.pack(pady=(10, 5))
        date_frame1 = tk.Frame(self)
        date_frame1.pack(pady=(0, 5))
        date_frame2 = tk.Frame(self)
        date_frame2.pack(pady=(0, 5))
        date_frame3 = tk.Frame(self)
        date_frame3.pack(pady=(0, 5))

        # Create a label
        label = tk.Label(date_frame1, text="Select Country/Continent: ")
        label.pack(pady=10)

        # Create a Combobox
        options = ['Asia','North','Europe','South','Oceania','Africa','World','China','USA','India','France','Germany','Brazil','S._Korea','Japan','Italy','UK','Russia','Turkey','Spain','Australia','Vietnam','Taiwan','Argentina','Netherlands','Mexico','Iran','Indonesia','Poland','Colombia','Greece','Austria','Portugal','Ukraine','Chile','Malaysia','Canada','Belgium','Israel','DPRK','Thailand','Czechia','Peru','Switzerland','Philippines','South','Romania','Denmark','Singapore','Hong','Sweden','Serbia','New','Iraq','Hungary','Bangladesh','Slovakia','Georgia','Jordan','Ireland','Pakistan','Finland','Norway','Kazakhstan','Lithuania','Slovenia','Bulgaria','Croatia','Guatemala','Morocco','Lebanon','Costa','Bolivia','Tunisia','Cuba','Ecuador','UAE','Panama','Uruguay','Mongolia','Nepal','Belarus','Latvia','Saudi','Paraguay','Azerbaijan','Bahrain','Cyprus','Dominican','Sri','Kuwait','Myanmar','Moldova','Estonia','Palestine','Venezuela','Egypt','Qatar','Libya','Ethiopia','Runion','Honduras','Armenia','Bosnia','Oman','Luxembourg','North','Zambia','Kenya','Brunei','Albania','Botswana','Montenegro','Algeria','Nigeria','Zimbabwe','Uzbekistan','Mozambique','Afghanistan','Martinique','Laos','Iceland','Kyrgyzstan','Guadeloupe','El','Trinidad','Maldives','Namibia','Uganda','Ghana','Jamaica','Cambodia','Rwanda','Cameroon','Malta','Barbados','Angola','Channel','DRC','French','Malawi','Senegal','Ivory','Suriname','New','French','Eswatini','Guyana','Belize','Fiji','Madagascar','Cabo','Sudan','Mauritania','Bhutan','Syria','Burundi','Seychelles','Gabon','Andorra','Papua','Curaao','Aruba','Tanzania','Mauritius','Mayotte','Togo','Guinea','Bahamas','Isle','Lesotho','Haiti','Faeroe','Mali','Cayman','Saint','Benin','Somalia','Micronesia','San','Solomon','Congo','Macao','Timor-Leste','Burkina','Liechtenstein','Gibraltar','Grenada','Bermuda','South','Nicaragua','Tajikistan','Equatorial','Monaco','Samoa','Tonga','Marshall','Dominica','Djibouti','CAR','Gambia','Saint','Vanuatu','Greenland','Yemen','Caribbean','Sint','Eritrea','Niger','St.','Guinea-Bissau','Comoros','Antigua','Liberia','Sierra','Chad','British','Cook','Sao','Turks','Saint','Palau','St.','Nauru','Kiribati','Anguilla','Wallis','Saint','Tuvalu','Saint','Falkland','Montserrat','Niue','Diamond','Tokelau','Vatican','Western','MS']
        options.sort()
        self.selected_option2 = tk.StringVar(self)
        self.selected_option2.set(options[0])  # Set default value
        dropdown = tk.OptionMenu(date_frame1, self.selected_option2, *options)
        dropdown.pack(pady=(0, 5))

        # Date Picker 1
        date_input1_label = tk.Label(date_frame2, text="Start Date:")
        date_input1_label.pack(side=tk.LEFT, padx=5)
        self.date_input1 = tk.Entry(date_frame2)
        self.date_input1.pack(side=tk.LEFT, padx=5)
        
        # Date Picker 2
        date_input2_label = tk.Label(date_frame3, text="End Date:")
        date_input2_label.pack(side=tk.LEFT, padx=5)
        self.date_input2 = tk.Entry(date_frame3)
        self.date_input2.pack(side=tk.LEFT, padx=5)

        # Execute Button
        execute_button = tk.Button(self, text="Execute", command=self.execute_program2)
        execute_button.pack(pady=10)

        button = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(StartPage))
        button.pack()

    def execute_program(self):
        option = self.selected_option.get()
        messagebox.showinfo("Execution Result", f"Country/Continent selected: {option}")
    def execute_program2(self):
        option = self.selected_option2.get()
        date1 = self.date_input1.get()
        date2 = self.date_input2.get()
        messagebox.showinfo("Execution Result", f"Country selected: {option} dates: [{date1},{date2}]")

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Module 3.2", font=("Helvetica", 18, "bold"))
        label.pack(pady=10,padx=10)
        # Section 1
        section1_label = tk.Label(self, text="Extract Worldwide data", font=("Helvetica", 16, "bold"))
        section1_label.pack(pady=(10, 5))
        date_frame1 = tk.Frame(self)
        date_frame1.pack(pady=(0, 5))
        date_frame2 = tk.Frame(self)
        date_frame2.pack(pady=(0, 5))
        
        # Date Picker 1
        date_input1_label = tk.Label(date_frame1, text="Start Date:")
        date_input1_label.pack(side=tk.LEFT, padx=5)
        self.date_input1 = tk.Entry(date_frame1)
        self.date_input1.pack(side=tk.LEFT, padx=5)
        
        # Date Picker 2
        date_input2_label = tk.Label(date_frame2, text="End Date:")
        date_input2_label.pack(side=tk.LEFT, padx=5)
        self.date_input2 = tk.Entry(date_frame2)
        self.date_input2.pack(side=tk.LEFT, padx=5)
        
        # Execute Button
        execute_button = tk.Button(self, text="Let's Extract Worldwide", command=self.execute_program)
        execute_button.pack(pady=10)
        
        # Section 2
        section2_label = tk.Label(self, text="Extract Country Data", font=("Helvetica", 16, "bold"))
        section2_label.pack(pady=10)
        # Dropdown
        options = ["India", "Australia", "Singapore", "Malaysia", "England"]
        self.selected_option = tk.StringVar(self)
        self.selected_option.set(options[0])  # Set default value
        dropdown = tk.OptionMenu(self, self.selected_option, *options)
        dropdown.pack(pady=(0, 5))
        
        # Date Entry Frames for Section 2
        date_frame3 = tk.Frame(self)
        date_frame3.pack(pady=(0, 5))
        date_frame4 = tk.Frame(self)
        date_frame4.pack(pady=(0, 5))
        
        # Date Input 3
        date_input3_label = tk.Label(date_frame3, text="Start Date:")
        date_input3_label.pack(side=tk.LEFT, padx=5)
        self.date_input3 = tk.Entry(date_frame3)
        self.date_input3.pack(side=tk.LEFT, padx=5)
        
        # Date Input 4
        date_input4_label = tk.Label(date_frame4, text="End Date:")
        date_input4_label.pack(side=tk.LEFT, padx=5)
        self.date_input4 = tk.Entry(date_frame4)
        self.date_input4.pack(side=tk.LEFT, padx=5)
        
        # Execute Button 2
        execute_button2 = tk.Button(self, text="Let's Extract Country", command=self.execute_program2)
        execute_button2.pack(pady=10)
        
        # Section 3
        section3_label = tk.Label(self, text="Calculate Jaccard Similarity", font=("Helvetica", 16, "bold"))
        section3_label.pack(pady=10)
        execute_button3 = tk.Button(self, text="Let's calculate similarity", command=self.execute_program3)
        execute_button3.pack(pady=10)
        
        button = tk.Button(self, text="Go Back!", command=lambda: controller.show_frame(StartPage))
        button.pack(pady=5)
    def execute_program(self):
        date1 = self.date_input1.get()
        date2 = self.date_input2.get()
        messagebox.showinfo("Execution Result", f"Dates selected:\nStart Date: {date1}\nEnd Date: {date2}")

    def execute_program2(self):
        date3 = self.date_input3.get()
        date4 = self.date_input4.get()
        option = self.selected_option.get()
        messagebox.showinfo("Execution Result", f"Option selected: {option}\nStart Date: {date3}\nEnd Date: {date4}")
        
    def execute_program3(self):
        option = self.selected_option.get()
        messagebox.showinfo("Execution Result", f"Country selected: {option}")

    
        
if __name__ == "__main__":
    app = worldometerCoronaApp()
    style = ttk.Style(app)
    style.theme_use('clam')
    app.geometry("1000x1000")
    app.mainloop()
