from app import GUI
from card_downloader import CardDownloader
from card_editor import CardEditor
import os

class PPM():
    def __init__(self):
        self.gui = GUI(self)
        self.cd = CardDownloader()
        self.ce = CardEditor()
        self.directory = ''
        self.filename = ''
        self.card_list = []
        self.found_cards = ''

    def make_proxies(self):
        self.process_image_list(self.filename)
        #exit()
        
        self.gui.append_status_label(f"Processed card list, found {len(self.card_list)} cards.\n")
        self.gui.append_status_label("Beginning card download. This could take some time...\n")

        self.download_all_cards()
        self.gui.append_status_label("All cards downloaded\n")
        self.gui.append_status_label("Fixing card borders and quality\n")
        self.fix_images()

    @staticmethod
    def fix_card_name(card_name):
        card_name = card_name[1:].strip().replace("Ã©", "e")
        if "(" in card_name:
            lb_index = card_name.find("(")
            rb_index = card_name.find(")") + 2
            l_card_name = card_name[:lb_index]
            r_card_name = card_name[rb_index:]
            card_name = l_card_name + r_card_name
        return card_name

    def process_image_list(self, filepath):
        with open(filepath, "r") as f:
            for line in f:
                if line[:1].isdigit() and len(line) > 0:
                    for _ in range(int(line[0])):
                        card_name = self.fix_card_name(line)
                        self.card_list.append(card_name)
                        print(card_name)
    

    
    def download_all_cards(self):
        for card_name in self.card_list:
            self.cd.download_image(card_name, self.directory)
            self.gui.append_status_label(f"Found {card_name}\n")
        self.gui.append_status_label("Completed downloading cards\n")

    def fix_images(self):
        for f in os.listdir(self.directory):
            filepath = os.path.join(self.directory, f)
            self.ce.add_border(filepath)
            self.ce.fix_dpi(filepath)
            self.gui.append_status_label(f"Fixed {f}\n")
            
        
        
    
    def run(self):
        self.gui.run()

if __name__ == "__main__":
    ppm = PPM()
    ppm.run()