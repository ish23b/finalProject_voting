from tkinter import *
import csv


class GUI:

    def __init__(self, window):

        self.cnt_jane = 0
        self.cnt_john = 0

        self.window = window

        ##### Voter ID enty
        self.frame_voterID = Frame(self.window)
        self.label_voterID = Label(self.frame_voterID, text='Voter ID #')
        self.entry_voterID = Entry(self.frame_voterID)

        # position Voter ID widgets and frame
        self.label_voterID.pack(padx=1, side='left')
        self.entry_voterID.pack(side='left')
        self.frame_voterID.pack(anchor='w', padx=10, pady=10)

        ##### Candidate selection
        self.frame_select = Frame(self.window)
        self.label_select = Label(self.frame_select, text='Choose candidate')
        self.radioStorage_select = IntVar()
        self.radioStorage_select.set(0)
        self.radio_select_Jane = Radiobutton(self.frame_select, text='Jane Jacobs', variable=self.radioStorage_select, value=1)
        self.radio_select_John = Radiobutton(self.frame_select, text='John Johnson', variable=self.radioStorage_select, value=2)

        # position candidate selection widgets and frame
        self.label_select.pack(padx=1, side='top')
        self.radio_select_Jane.pack(padx=5, side='top')
        self.radio_select_John.pack(padx=5, side='top')
        self.frame_select.pack(anchor='w', padx=10, pady=20)

        ##### submit vote
        self.frame_vote = Frame(self.window)
        self.button_vote = Button(self.frame_vote, text='VOTE', command=self.submit)

        # position submit button
        self.button_vote.pack()
        self.frame_vote.pack(pady=5)

        ##### instructions
        self.frame_instr = Frame(self.window)
        self.label_instr = Label(self.frame_instr, text='Instructions')
        self.label_instr2 = Label(self.frame_instr, text='')
        self.label_instr.pack()
        self.label_instr2.pack()
        self.frame_instr.pack(pady=10)

        #### refresh button
        self.frame_refresh = Frame(self.window)
        self.button_refresh = Button(self.frame_refresh, text='REFRESH', command=self.reset)

        # position submit button
        self.button_refresh.pack()
        #self.frame_refresh.pack(pady=12)

    # keeps track of the vote count
    # displays the final output
    # returns no value
    def submit(self):
        try:
            id = int(self.entry_voterID.get().strip())
            choice_int = self.radioStorage_select.get()
            if choice_int == 1:
                self.cnt_jane += 1
                choice_str = "Jane"
            elif choice_int == 2:
                self.cnt_john += 1
                choice_str = "John"

            outrow = [id, choice_str, self.cnt_jane, self.cnt_john]
            with open('election_results.csv', 'a', newline='') as output_csv_file:
                content = csv.writer(output_csv_file)
                content.writerow(outrow)

            self.label_instr.config(text="Thank you for your vote.")
            self.label_instr2.config(text="Click 'refresh' for the next voter.")
            self.frame_refresh.pack(pady=12)

        except:
            self.label_instr.config(text="Enter correct voter ID.")
            self.entry_voterID.delete(0, END)

    def reset(self):
        self.label_instr.config(text="")
        self.label_instr2.config(text="")
        self.frame_refresh.pack_forget()
        self.entry_voterID.delete(0, END)
        self.radioStorage_select.set(0)



