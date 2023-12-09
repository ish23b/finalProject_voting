from gui import *


def main() -> None:

    with open('election_results.csv', 'w', newline='') as output_csv_file:
        voting_csv_writer = csv.writer(output_csv_file)
        # write header row for csv file
        voting_csv_writer.writerow(['Voter_ID', 'Choice', 'RunningTotal_Jane', 'RunningTotal_John'])

    window = Tk()
    window.title('Election')
    window.geometry('240x300')
    window.resizable(False, False)
    GUI(window)

    window.mainloop()



if __name__ == '__main__':
    main()