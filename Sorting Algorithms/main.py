from stalinsort import StalinSort
from diddysort import DiddySort
from sixsevensort import SixSevenSort 



def main() -> None:
     nums = [14,6,18,26,23,10,7,2,19,95,6,94,10,7]
     stalin = StalinSort()
     diddy = DiddySort()
     sixseven = SixSevenSort()
     validsorts = {
            "Stalin": stalin,
            "Diddy": diddy,
            "Six": sixseven
            }
     
     print(f"List: {nums}")
     while True:
            sorttype = input("Hello, user! What sort would you like to use to sort the list?: ").strip().title()
            if sorttype in validsorts:
                  sorted_list = validsorts[sorttype].sort(nums)
                  print(sorted_list)
                  break
            else:
                  print("Thats not a valid sort.")

    

if __name__ == '__main__':
     main()