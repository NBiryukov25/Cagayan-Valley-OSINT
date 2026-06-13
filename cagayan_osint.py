#!/usr/bin/env python3
import csv
import urllib.parse
from datetime import datetime


class CagayanValleyOSINT:
    def __init__(self):
        self.dorks = []
        
    def get_inputs(self):
        print("\n" + "="*60)
        print("📍 CAGAYAN VALLEY OSINT TOOL")
        print("   Tuguegarao City | Cagayan Province | Region II")
        print("="*60 + "\n")
        
        inputs = {}
        print("Enter search targets (press Enter to skip):")
        print("-" * 50)
        
        inputs['target_name'] = input("Person/Entity Name: ").strip()
        inputs['business'] = input("Business/Organization: ").strip()
        inputs['barangay'] = input("Barangay/Area: ").strip()
        inputs['topic'] = input("Topic/Event: ").strip()
        inputs['phone'] = input("Phone Number: ").strip()
        inputs['vehicle'] = input("Vehicle/Plate Info: ").strip()
        
        print("\n" + "-" * 50)
        print("INCIDENT TYPES (y/n):")
        print("-" * 50)
        
        inputs['natural_disaster'] = input("Include natural disaster searches? (y/n): ").strip().lower() == 'y'
        inputs['accident'] = input("Include accident searches? (y/n): ").strip().lower() == 'y'
        inputs['political'] = input("Include political event searches? (y/n): ").strip().lower() == 'y'
        
        if inputs['natural_disaster']:
            print("\nNatural disaster types:")
            inputs['disaster_type'] = input("Specific type (typhoon/flood/earthquake/landslide/all): ").strip().lower() or "all"
        
        if inputs['political']:
            print("\nPolitical event types:")
            inputs['political_type'] = input("Type (election/protest/corruption/violence/all): ").strip().lower() or "all"
        
        return inputs
    
    def make_url(self, query):
        return f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    
    def generate_dorks(self, inputs):
        name = inputs.get('target_name', '')
        biz = inputs.get('business', '')
        brgy = inputs.get('barangay', '')
        topic = inputs.get('topic', '')
        phone = inputs.get('phone', '')
        vehicle = inputs.get('vehicle', '')
        
        natural_disaster = inputs.get('natural_disaster', False)
        accident = inputs.get('accident', False)
        political = inputs.get('political', False)
        disaster_type = inputs.get('disaster_type', 'all')
        political_type = inputs.get('political_type', 'all')
        
        tuguegarao = "Tuguegarao"
        cagayan = "Cagayan"
        valley = "Cagayan Valley"
        
        # === NATURAL DISASTERS ===
        if natural_disaster:
            if disaster_type in ['typhoon', 'all']:
                self.dorks.extend([
                    ('typhoon "Tuguegarao" site:pagasa.dost.gov.ph', "Disaster", "PAGASA Typhoon", "High"),
                    ('typhoon "Cagayan" damage', "Disaster", "Typhoon Damage", "High"),
                    ('typhoon "Cagayan Valley" flooding', "Disaster", "Typhoon Floods", "High"),
                    ('"Bagyong" "Cagayan" site:newsbytes.ph', "Disaster", "Typhoon Newsbytes", "Medium"),
                    ('"signal number" "Cagayan" typhoon', "Disaster", "Typhoon Signal", "Medium"),
                ])
            
            if disaster_type in ['flood', 'all']:
                self.dorks.extend([
                    ('flooding "Tuguegarao City"', "Disaster", "Tuguegarao Floods", "High"),
                    ('"Cagayan River" flood overflow', "Disaster", "Cagayan River Flood", "High"),
                    ('floods "Cagayan" rescue evacuation', "Disaster", "Flood Rescue", "High"),
                    ('"Cagayan Valley" inundation', "Disaster", "Valley Flooding", "Medium"),
                    ('"barangay" flooded "Cagayan"', "Disaster", "Barangay Floods", "Medium"),
                ])
            
            if disaster_type in ['earthquake', 'all']:
                self.dorks.extend([
                    ('earthquake "Cagayan" PHIVOLCS', "Disaster", "Earthquake PHIVOLCS", "High"),
                    ('"linog" "Cagayan Valley"', "Disaster", "Earthquake Local Term", "Medium"),
                    ('earthquake damage "Tuguegarao"', "Disaster", "Earthquake Damage", "Medium"),
                ])
            
            if disaster_type in ['landslide', 'all']:
                self.dorks.extend([
                    ('landslide "Cagayan" casualty', "Disaster", "Landslide Casualty", "High"),
                    ('"pagguho" "Cagayan"', "Disaster", "Landslide Local", "Medium"),
                    ('landslide "Tuguegarao" road blocked', "Disaster", "Landslide Road", "Medium"),
                ])
            
            # General disaster response
            self.dorks.extend([
                ('NDRRMC "Cagayan" update', "Disaster", "NDRRMC Updates", "High"),
                ('"disaster response" "Cagayan Valley"', "Disaster", "Disaster Response", "Medium"),
                ('evacuation center "Tuguegarao"', "Disaster", "Evacuation Centers", "Medium"),
                ('relief goods "Cagayan" distribution', "Disaster", "Relief Operations", "Low"),
            ])
        
        # === ACCIDENTS ===
        if accident:
            self.dorks.extend([
                ('accident "Tuguegarao" today', "Accident", "Tuguegarao Accidents", "High"),
                ('"vehicular accident" "Cagayan"', "Accident", "Vehicular Accidents", "High"),
                ('"banggaan" "Cagayan" sasakyan', "Accident", "Accident Local Term", "Medium"),
                ('crash "Cagayan Valley" bus truck', "Accident", "Bus/Truck Crashes", "Medium"),
                ('"motorcycle accident" "Tuguegarao"', "Accident", "Motorcycle Accidents", "Medium"),
                ('"hit and run" "Cagayan"', "Accident", "Hit and Run", "Medium"),
                ('" aksidente" "Cagayan" patay sugatan', "Accident", "Accident Casualty", "High"),
                ('maritime incident "Aparri" "Cagayan"', "Accident", "Maritime Aparri", "Medium"),
                ('boat capsized "Cagayan River"', "Accident", "Boat Incident", "Medium"),
                ('construction collapse "Cagayan"', "Accident", "Infrastructure Accident", "Low"),
                ('fire "Tuguegarao" BFP', "Accident", "Fire Incidents", "Medium"),
                ('"sunog" "Cagayan" bahay', "Accident", "Fire Local Term", "Medium"),
            ])
        
        # === POLITICAL EVENTS ===
        if political:
            if political_type in ['election', 'all']:
                self.dorks.extend([
                    ('election "Cagayan" Comelec', "Political", "Election Comelec", "High"),
                    ('"halalan" "Cagayan" resulta', "Political", "Election Results", "High"),
                    ('vote buying "Cagayan" report', "Political", "Vote Buying", "High"),
                    ('election violence "Cagayan Valley"', "Political", "Election Violence", "High"),
                    ('"campaign rally" "Tuguegarao"', "Political", "Campaign Rallies", "Medium"),
                    ('candidates "Cagayan" provincial', "Political", "Provincial Candidates", "Medium"),
                    ('"board member" "Cagayan" election', "Political", "Board Member Race", "Medium"),
                    ('mayor "Tuguegarao" election', "Political", "Mayoral Election", "High"),
                ])
            
            if political_type in ['protest', 'all']:
                self.dorks.extend([
                    ('protest "Tuguegarao" rally', "Political", "Tuguegarao Protests", "High"),
                    ('"kilos protesta" "Cagayan"', "Political", "Protest Local Term", "Medium"),
                    ('demonstration "Cagayan" PNP', "Political", "Demonstrations", "Medium"),
                    ('"transport strike" "Cagayan Valley"', "Political", "Transport Strikes", "Medium"),
                    ('rally "Cagayan" students', "Political", "Student Protests", "Low"),
                ])
            
            if political_type in ['corruption', 'all']:
                self.dorks.extend([
                    ('corruption "Cagayan" Ombudsman', "Political", "Corruption Cases", "High"),
                    ('"anomalya" "Cagayan" probinsya', "Political", "Anomaly Local Term", "Medium"),
                    ('graft "Cagayan" mayor governor', "Political", "Graft Cases", "High"),
                    ('"pork barrel" "Cagayan" congressman', "Political", "Pork Barrel", "Medium"),
                    ('irregularity "Cagayan" procurement', "Political", "Procurement Issues", "Medium"),
                    ('suspension "Cagayan" official', "Political", "Official Suspension", "High"),
                ])
            
            if political_type in ['violence', 'all']:
                self.dorks.extend([
                    ('ambush "Cagayan" politician', "Political", "Political Ambush", "High"),
                    ('"political killing" "Cagayan Valley"', "Political", "Political Killings", "High"),
                    ('"riding in tandem" "Cagayan"', "Political", "Riding in Tandem", "High"),
                    ('shooting "Cagayan" barangay', "Political", "Barangay Violence", "Medium"),
                    ('"private armed group" "Cagayan"', "Political", "Private Armies", "Medium"),
                    ('election related violence Cagayan', "Political", "ERI Cagayan", "High"),
                ])
            
            # General political
            self.dorks.extend([
                ('politics "Cagayan" controversy', "Political", "Political Controversy", "Medium"),
                ('dynasty "Cagayan" family', "Political", "Political Dynasty", "Low"),
            ])
        
        # === LOCAL NEWS MEDIA ===
        if name:
            self.dorks.extend([
                (f'"{name}" site:tribune.net.ph', "LocalNews", "Daily Tribune", "High"),
                (f'"{name}" site:manilatimes.net', "LocalNews", "Manila Times", "High"),
                (f'"{name}" site:newsbytes.ph', "LocalNews", "Newsbytes", "Medium"),
                (f'"{name}" "Cagayan" site:facebook.com', "Social", "Facebook Mentions", "High"),
                (f'"{name}" site:abs-cbn.com "Cagayan"', "LocalNews", "ABS-CBN Regional", "Medium"),
                (f'"{name}" site:gmanetwork.com "Cagayan"', "LocalNews", "GMA Regional", "Medium"),
            ])
        
        if topic:
            self.dorks.extend([
                (f'"{topic}" "{tuguegarao}"', "LocalNews", "Topic in Tuguegarao", "High"),
                (f'"{topic}" "{cagayan}" site:newsbytes.ph', "LocalNews", "Topic Newsbytes", "High"),
                (f'"{topic}" "Cagayan Valley"', "LocalNews", "Topic Valley-wide", "Medium"),
            ])
        
        # === SOCIAL & COMMUNITY ===
        if name or biz:
            target = name or biz
            self.dorks.extend([
                (f'"{target}" "Tuguegarao" site:facebook.com', "Social", "FB Tuguegarao", "High"),
                (f'"{target}" "Cagayan" site:facebook.com', "Social", "FB Cagayan", "High"),
                (f'"{target}" site:twitter.com "Tuguegarao"', "Social", "Twitter/X Local", "Medium"),
                (f'"{target}" site:instagram.com "Tuguegarao"', "Social", "Instagram Local", "Medium"),
                (f'"{target}" "Cagayan" site:reddit.com', "Social", "Reddit Mentions", "Low"),
            ])
        
        # === BARANGAY & COMMUNITY ===
        if brgy:
            self.dorks.extend([
                (f'"{brgy}" "barangay" "Tuguegarao" site:facebook.com', "Community", "Barangay FB Page", "High"),
                (f'"{brgy}" "Tuguegarao City"', "Community", "Barangay Mentions", "Medium"),
                (f'site:facebook.com "{brgy}" Cagayan', "Community", "FB Barangay Search", "Medium"),
            ])
        
        # === GOVERNMENT & OFFICIAL ===
        if name or biz:
            target = name or biz
            self.dorks.extend([
                (f'"{target}" site:tuguegaraocity.gov.ph', "Govt", "City Gov Website", "High"),
                (f'"{target}" site:cagayan.gov.ph', "Govt", "Provincial Gov", "High"),
                (f'"{target}" "DILG" "Cagayan"', "Govt", "DILG Records", "Medium"),
                (f'"{target}" "BIR" "Tuguegarao"', "Govt", "BIR Regional", "Medium"),
                (f'"{target}" "SEC" "Cagayan"', "Govt", "SEC Registration", "Low"),
            ])
        
        # === UNIVERSITIES & EDUCATION ===
        if name:
            self.dorks.extend([
                (f'"{name}" site:csu.edu.ph', "Education", "CSU Records", "High"),
                (f'"{name}" "Cagayan State University"', "Education", "CSU Mentions", "High"),
                (f'"{name}" "SMCT" "Tuguegarao"', "Education", "SMCT Records", "Medium"),
                (f'"{name}" "University of Cagayan Valley"', "Education", "UCV Mentions", "Medium"),
                (f'"{name}" site:ustuguegarao.edu.ph', "Education", "UST Cagayan", "Low"),
            ])
        
        # === BUSINESS & COMMERCE ===
        if biz:
            self.dorks.extend([
                (f'"{biz}" "Tuguegarao" "business"', "Business", "Business Registry", "High"),
                (f'"{biz}" site:dti.gov.ph "Cagayan"', "Business", "DTI Registration", "Medium"),
                (f'"{biz}" "Tuguegarao" site:yellowpages.ph', "Business", "Yellow Pages", "Medium"),
                (f'"{biz}" "Cagayan" directory', "Business", "Local Directory", "Low"),
            ])
        
        # === CLASSIFIEDS & MARKETPLACE ===
        if name or biz or topic:
            search_term = name or biz or topic
            self.dorks.extend([
                (f'"{search_term}" site:facebook.com/marketplace "Tuguegarao"', "Marketplace", "FB Marketplace", "Medium"),
                (f'"{search_term}" "Tuguegarao" site:carousell.ph', "Marketplace", "Carousell Local", "Medium"),
                (f'"{search_term}" site:olx.ph "Cagayan"', "Marketplace", "OLX Cagayan", "Low"),
                (f'"{search_term}" "for sale" "Tuguegarao"', "Marketplace", "Local For Sale", "Low"),
            ])
        
        # === CONTACT & IDENTIFIERS ===
        if phone:
            self.dorks.extend([
                (f'"{phone}" "Tuguegarao"', "Contact", "Phone Local", "High"),
                (f'"{phone}" "Cagayan"', "Contact", "Phone Regional", "High"),
                (f'"{phone}" site:facebook.com', "Contact", "Phone on FB", "Medium"),
            ])
        
        if vehicle:
            self.dorks.extend([
                (f'"{vehicle}" "Tuguegarao"', "Vehicle", "Vehicle Local", "Medium"),
                (f'"{vehicle}" "Cagayan" "LTO"', "Vehicle", "LTO Records", "Low"),
            ])
        
        # === EMERGENCY & INCIDENT (General) ===
        if topic:
            self.dorks.extend([
                (f'"{topic}" "PNP" "Tuguegarao"', "Incident", "Police Reports", "Medium"),
                (f'"{topic}" "BFP" "Cagayan"', "Incident", "Fire Dept Records", "Low"),
            ])
        
        # === HISTORICAL & ARCHIVE ===
        if name or topic:
            target = name or topic
            self.dorks.extend([
                (f'"{target}" "Tuguegarao" site:web.archive.org', "Archive", "Wayback Machine", "Low"),
                (f'cache:"{target}" "Cagayan"', "Archive", "Cached Results", "Low"),
            ])
        
        return self.dorks
    
    def export_to_csv(self, filename=None):
        if not filename:
            filename = f"cagayan_osint_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        sorted_dorks = sorted(self.dorks, key=lambda x: ({"High": 0, "Medium": 1, "Low": 2}.get(x[3], 3), x[0]))
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Priority', 'Category', 'Source', 'Query', 'Google_URL'])
            
            for query, category, source, priority in sorted_dorks:
                url = self.make_url(query)
                writer.writerow([priority, category, source, query, url])
        
        print(f"\n💾 Saved: {filename}")
        print(f"📊 Total dorks: {len(sorted_dorks)}")
        
        categories = {}
        for _, cat, _, pri in sorted_dorks:
            key = f"{cat} ({pri})"
            categories[key] = categories.get(key, 0) + 1
        
        print(f"\n📋 Breakdown:")
        for cat, count in sorted(categories.items()):
            print(f"   {cat}: {count}")
        
        return filename
    
    def run(self):
        inputs = self.get_inputs()
        
        print("\n🔄 Generating Cagayan Valley OSINT dorks...")
        self.generate_dorks(inputs)
        print(f"✅ Generated {len(self.dorks)} location-specific dorks")
        
        self.export_to_csv()


if __name__ == "__main__":
    tool = CagayanValleyOSINT()
    tool.run()
