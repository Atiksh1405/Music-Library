import tkinter as tk
from tkinter import messagebox
import webbrowser

search_pages = {
    "ar rahman": lambda: open_ar_rahman_page(root),

    "agar main kahoon": lambda: open_ar_rahman_page(root),

    "dil bechara": lambda: open_ar_rahman_page(root),

    "dil se ra": lambda: open_ar_rahman_page(root),

    "jai ho": lambda: open_ar_rahman_page(root),

    "kun faya kun": lambda: open_ar_rahman_page(root),

    "luka chuppi": lambda: open_ar_rahman_page(root),

    "maahi ve": lambda: open_ar_rahman_page(root),

    "maa tujhe salaam": lambda: open_ar_rahman_page(root),

    "o paalanhaare": lambda: open_ar_rahman_page(root),

    "tum mile": lambda: open_ar_rahman_page(root),


    "arijit singh": lambda: open_arijit_singh_page(root),

    "channa mereya": lambda: open_arijit_singh_page(root),

    "har kisi ko": lambda: open_arijit_singh_page(root),

    "kabira": lambda: open_arijit_singh_page(root),

    "o bedardeya": lambda: open_arijit_singh_page(root),

    "pachtaoge": lambda: open_arijit_singh_page(root),

    "pyaar hona kayi baar hai": lambda: open_arijit_singh_page(root),

    "raabta": lambda: open_arijit_singh_page(root),

    "soulmate": lambda: open_arijit_singh_page(root),

    "tera ban jaunga": lambda: open_arijit_singh_page(root),

    "tum hi ho": lambda: open_arijit_singh_page(root),


    "kk": lambda: open_kk_page(root),

    "ankhon mein teri": lambda: open_kk_page(root),

    "dil ibaadat": lambda: open_kk_page(root),

    "dil kyun yeh mera": lambda: open_kk_page(root),

    "hasi": lambda: open_kk_page(root),

    "khuda jaane": lambda: open_kk_page(root),

    "make some noise for the desi boyz": lambda: open_kk_page(root),

    "pyaar ke pal": lambda: open_kk_page(root),

    "tadap tadap": lambda: open_kk_page(root),

    "yaaron": lambda: open_kk_page(root),

    "zindagi do pal ki": lambda: open_kk_page(root),


    "pritam chakraborty": lambda: open_pritam_chakraborty_page(root),

    "aahun aahun": lambda: open_pritam_chakraborty_page(root),

    "ajj din chadheya": lambda: open_pritam_chakraborty_page(root),

    "baarish": lambda: open_pritam_chakraborty_page(root),

    "channa mereya": lambda: open_pritam_chakraborty_page(root),

    "chor bazaari": lambda: open_pritam_chakraborty_page(root),

    "Kabira": lambda: open_pritam_chakraborty_page(root),

    "pee loon": lambda: open_pritam_chakraborty_page(root),

    "subha hone na de": lambda: open_pritam_chakraborty_page(root),

    "tum hi ho bandhu": lambda: open_pritam_chakraborty_page(root),

    "zindagi do pal ki": lambda: open_pritam_chakraborty_page(root),


    "sanam": lambda: open_sanam_page(root),

    "aap ki nazron ne samjha": lambda: open_sanam_page(root),

    "ek ladki ko dekha to": lambda: open_sanam_page(root),

    "gulabi aankhen": lambda: open_sanam_page(root),

    "hai apna dil to awara": lambda: open_sanam_page(root),

    "lag jaa gale": lambda: open_sanam_page(root),

    "mere mehboob qayamat hogi": lambda: open_sanam_page(root),

    "o mere dil ke chain": lambda: open_sanam_page(root),

    "pehla nasha": lambda: open_sanam_page(root),

    "tujhse naraz nahi zindagi": lambda: open_sanam_page(root),

    "yeh raaten yeh mausam": lambda: open_sanam_page(root),


    "ap dhillon": lambda: open_ap_dhillon_page(root),

    "arrogant": lambda: open_ap_dhillon_page(root),

    "brown munde": lambda: open_ap_dhillon_page(root),

    "excuses": lambda: open_ap_dhillon_page(root),

    "final thoughts": lambda: open_ap_dhillon_page(root),

    "saada pyaar": lambda: open_ap_dhillon_page(root),

    "sleepless": lambda: open_ap_dhillon_page(root),

    "summer high": lambda: open_ap_dhillon_page(root),

    "toxic": lambda: open_ap_dhillon_page(root),

    "true stories": lambda: open_ap_dhillon_page(root),

    "with you": lambda: open_ap_dhillon_page(root),


    "diljit dosanjh": lambda: open_diljit_dosanjh_page(root),

    "born to shine": lambda: open_diljit_dosanjh_page(root),

    "do you know": lambda: open_diljit_dosanjh_page(root),

    "g.o.a.t.": lambda: open_diljit_dosanjh_page(root),

    "hass hass": lambda: open_diljit_dosanjh_page(root),

    "kinni kinni": lambda: open_diljit_dosanjh_page(root),

    "lalkara": lambda: open_diljit_dosanjh_page(root),

    "lover": lambda: open_diljit_dosanjh_page(root),

    "magic": lambda: open_diljit_dosanjh_page(root),

    "patiala peg": lambda: open_diljit_dosanjh_page(root),

    "sauda khara khara": lambda: open_diljit_dosanjh_page(root),


    "karan aujla": lambda: open_karan_aujla_page(root),

    "52 bars": lambda: open_karan_aujla_page(root),

    "admirin' you": lambda: open_karan_aujla_page(root),

    "bachke bachke": lambda: open_karan_aujla_page(root),

    "chitta kurta": lambda: open_karan_aujla_page(root),

    "jee ni lagda": lambda: open_karan_aujla_page(root),

    "players": lambda: open_karan_aujla_page(root),

    "softly": lambda: open_karan_aujla_page(root),

    "tauba tauba": lambda: open_karan_aujla_page(root),

    "white brown black": lambda: open_karan_aujla_page(root),

    "winning speech": lambda: open_karan_aujla_page(root),


    "rabbi shergill": lambda: open_rabbi_shergill_page(root),

    "bandiya tu": lambda: open_rabbi_shergill_page(root),

    "bulla ki jana": lambda: open_rabbi_shergill_page(root),

    "bulleya": lambda: open_rabbi_shergill_page(root),

    "challa": lambda: open_rabbi_shergill_page(root),

    "gill te guitar": lambda: open_rabbi_shergill_page(root),

    "ishtihar": lambda: open_rabbi_shergill_page(root),

    "jugni": lambda: open_rabbi_shergill_page(root),

    "pahilan": lambda: open_rabbi_shergill_page(root),

    "tere bin": lambda: open_rabbi_shergill_page(root),

    "totia manmotia": lambda: open_rabbi_shergill_page(root),


    "yo yo honey singh": lambda: open_honey_singh_page(root),

    "alcoholic": lambda: open_honey_singh_page(root),
    
    "angreji beat": lambda: open_honey_singh_page(root),

    "brown rang": lambda: open_honey_singh_page(root),

    "chaar botal vodka": lambda: open_honey_singh_page(root),

    "desi kalakaar": lambda: open_honey_singh_page(root),

    "dope shope": lambda: open_honey_singh_page(root),

    "khadke glassy": lambda: open_honey_singh_page(root),

    "love dose": lambda: open_honey_singh_page(root),

    "manali trance": lambda: open_honey_singh_page(root),

    "one bottle down": lambda: open_honey_singh_page(root),


    "ali sethi": lambda: open_ali_sethi_page(root),

    "aaqa abida": lambda: open_ali_sethi_page(root),

    "chan kithan": lambda: open_ali_sethi_page(root),

    "dil ki khair": lambda: open_ali_sethi_page(root),

    "ghazab kiya": lambda: open_ali_sethi_page(root),

    "gulon main rang": lambda: open_ali_sethi_page(root),

    "honthon pe bas": lambda: open_ali_sethi_page(root),

    "mere aur hein iraaday": lambda: open_ali_sethi_page(root),

    "pasoori": lambda: open_ali_sethi_page(root),

    "rung": lambda: open_ali_sethi_page(root),

    "zindagi hai ajnabi": lambda: open_ali_sethi_page(root),


    "atif aslam": lambda: open_atif_aslam_page(root),

    "baarish": lambda: open_atif_aslam_page(root),

    "dil meri na sune": lambda: open_atif_aslam_page(root),

    "jab koi baat": lambda: open_atif_aslam_page(root),

    "jeena jeena": lambda: open_atif_aslam_page(root),

    "khair mangda": lambda: open_atif_aslam_page(root),

    "o saathi": lambda: open_atif_aslam_page(root),

    "tera hua": lambda: open_atif_aslam_page(root),

    "tere sang yaara": lambda: open_atif_aslam_page(root),

    "tu jaane na": lambda: open_atif_aslam_page(root),

    "woh lamhe woh baatein": lambda: open_atif_aslam_page(root),


    "aur": lambda: open_aur_page(root),

    "aaja mahi": lambda: open_aur_page(root),

    "chal diye tum kahan": lambda: open_aur_page(root),

    "dooriyan": lambda: open_aur_page(root),

    "kabhi mein kabhi tum": lambda: open_aur_page(root),

    "kya chahiye": lambda: open_aur_page(root),

    "never": lambda: open_aur_page(root),

    "no way to nowhere": lambda: open_aur_page(root),

    "shikayat": lambda: open_aur_page(root),

    "sometimes": lambda: open_aur_page(root),

    "tu hai kahan": lambda: open_aur_page(root),


    "nusrat fateh ali khan": lambda: open_nusrat_page(root),

    "aankh uthi mohabbat ne": lambda: open_nusrat_page(root),

    "afreen afreen": lambda: open_nusrat_page(root),

    "ghaus ul azam sha e jilani": lambda: open_nusrat_page(root),

    "jhoom jhoom jhoom baba": lambda: open_nusrat_page(root),

    "kaisa yeh pyaar hai allah allah": lambda: open_nusrat_page(root),

    "kali kali zulfon ke phande na": lambda: open_nusrat_page(root),

    "kinna sohna tenu rab ne banaya": lambda: open_nusrat_page(root),

    "mera piya ghar aaya": lambda: open_nusrat_page(root),

    "tajdar-e-haram": lambda: open_nusrat_page(root),

    "tumhein dilagi bhool jaani paray gi": lambda: open_nusrat_page(root),


    "shae gill": lambda: open_shae_gill_page(root),

    "bulleya": lambda: open_shae_gill_page(root),

    "dil-e-veeran": lambda: open_shae_gill_page(root),

    "gulabi ankheyn": lambda: open_shae_gill_page(root),

    "left right": lambda: open_shae_gill_page(root),

    "mera sawera": lambda: open_shae_gill_page(root),

    "one love": lambda: open_shae_gill_page(root),

    "pasoori": lambda: open_shae_gill_page(root),

    "sab sitaray humaray": lambda: open_shae_gill_page(root),

    "sukoon": lambda: open_shae_gill_page(root),

    "wo humsafar tha": lambda: open_shae_gill_page(root),


    "charlie puth": lambda: open_charlie_puth_page(root),

    "attention": lambda: open_charlie_puth_page(root),

    "done for me": lambda: open_charlie_puth_page(root),

    "how long": lambda: open_charlie_puth_page(root),

    "light switch": lambda: open_charlie_puth_page(root),

    "marvin gaye": lambda: open_charlie_puth_page(root),

    "one call away": lambda: open_charlie_puth_page(root),

    "see you again": lambda: open_charlie_puth_page(root),

    "the way i am": lambda: open_charlie_puth_page(root),

    "we don't talk anymore": lambda: open_charlie_puth_page(root),

    "when you're sad i'm sad": lambda: open_charlie_puth_page(root),


    "dua lipa": lambda: open_dua_lipa_page(root),

    "break my heart": lambda: open_dua_lipa_page(root),

    "don't start now": lambda: open_dua_lipa_page(root),

    "hallucinate": lambda: open_dua_lipa_page(root),

    "idgaf": lambda: open_dua_lipa_page(root),

    "levitating": lambda: open_dua_lipa_page(root),

    "love again": lambda: open_dua_lipa_page(root),

    "new rules": lambda: open_dua_lipa_page(root),

    "one kiss": lambda: open_dua_lipa_page(root),

    "physical": lambda: open_dua_lipa_page(root),

    "we're good": lambda: open_dua_lipa_page(root),


    "ed sheeran": lambda: open_ed_sheeran_page(root),

    "bad habits": lambda: open_ed_sheeran_page(root),

    "castle on the hill": lambda: open_ed_sheeran_page(root),

    "galway girl": lambda: open_ed_sheeran_page(root),

    "i don't care": lambda: open_ed_sheeran_page(root),

    "perfect": lambda: open_ed_sheeran_page(root),

    "photograph": lambda: open_ed_sheeran_page(root),

    "shivers": lambda: open_ed_sheeran_page(root),

    "shape of you": lambda: open_ed_sheeran_page(root),

    "thinking out loud": lambda: open_ed_sheeran_page(root),

    "the a team": lambda: open_ed_sheeran_page(root),


    "justin bieber": lambda: open_justin_bieber_page(root),

    "baby": lambda: open_justin_bieber_page(root),

    "ghost": lambda: open_justin_bieber_page(root),

    "intentions": lambda: open_justin_bieber_page(root),

    "let me love you": lambda: open_justin_bieber_page(root),

    "love yourself": lambda: open_justin_bieber_page(root),

    "never say never": lambda: open_justin_bieber_page(root),

    "peaches": lambda: open_justin_bieber_page(root),

    "sorry": lambda: open_justin_bieber_page(root),

    "stay": lambda: open_justin_bieber_page(root),

    "yummy": lambda: open_justin_bieber_page(root),


    "one direction": lambda: open_one_direction_page(root),

    "best song ever": lambda: open_one_direction_page(root),

    "drag me down": lambda: open_one_direction_page(root),

    "history": lambda: open_one_direction_page(root),

    "night changes": lambda: open_one_direction_page(root),

    "olivia": lambda: open_one_direction_page(root),

    "perfect": lambda: open_one_direction_page(root),

    "steal my girl": lambda: open_one_direction_page(root),

    "story of my life": lambda: open_one_direction_page(root),

    "what makes you beautiful": lambda: open_one_direction_page(root),

    "you & i": lambda: open_one_direction_page(root),
    }

def open_link(url):
    webbrowser.open(url)

def search():
    query = search_entry.get().strip().lower()
    if query:
        if query in search_pages:
            search_pages[query]()
        else:
            messagebox.showwarning("Not Found", f"No page found for: {query}")
    else:
        messagebox.showwarning("Empty Search", "Please enter a search query.")

def open_ar_rahman_page(hindi_window):
    hindi_window.withdraw()
    
    rahman_window = tk.Tk()
    rahman_window.title("AR Rahman Library")
    
    rahman_label = tk.Label(rahman_window, text="AR Rahman Music Collection")
    rahman_label.pack(pady=20)

    link1_button = tk.Button(rahman_window, text="Agar Main Kahoon", command=lambda: open_link("https://drive.google.com/file/d/10OYXtwqup4GDRcQRypZVnNvV2c4hTLWe/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(rahman_window, text="Dil Bechara", command=lambda: open_link("https://drive.google.com/file/d/1xUeqk4DjMVAGgIL1wKmzbpt7auhGZ3vI/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(rahman_window, text="Dil Se Ra", command=lambda: open_link("https://drive.google.com/file/d/11-7qlYFESU99UXFIxseMEtGw9rB7qBvs/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(rahman_window, text="Jai Ho", command=lambda: open_link("https://drive.google.com/file/d/1T-NMttrJvH7z2xHjE9tzkCXvAIz69EiB/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(rahman_window, text="Kun Faya Kun", command=lambda: open_link("https://drive.google.com/file/d/1r9mm-WoFunx7SZhVr-Yy7oXHS68j4zYM/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(rahman_window, text="Luka Chuppi", command=lambda: open_link("https://drive.google.com/file/d/1MCAame4pcZy73RrZ3c3Zo_kpEWvYtR6b/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(rahman_window, text="Maahi Ve", command=lambda: open_link("https://drive.google.com/file/d/1p-JrLwV7-iYNFbxzgU1Yh696vzHMsMjY/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(rahman_window, text="Maa Tujhe Salaam", command=lambda: open_link("https://drive.google.com/file/d/1PzHCmujdJKNA4zDqsnYJEhz2wxI8HgRP/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(rahman_window, text="O Paalanhaare", command=lambda: open_link("https://drive.google.com/file/d/1T4j3IeFB1OWX1ET9N9KjDZ85zNtArVx7/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(rahman_window, text="Tum Mile", command=lambda: open_link("https://drive.google.com/file/d/1E00QwWp5qmKNjbhiDv0SLneMdWjPPdqT/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(rahman_window, text="Back to Home", command=lambda: return_to_home(rahman_window)).pack(pady=10)

    rahman_window.mainloop()

def open_arijit_singh_page(hindi_window):
    hindi_window.withdraw()
    
    arijit_window = tk.Tk()
    arijit_window.title("Arijit Singh Library")
    
    arijit_label = tk.Label(arijit_window, text="Arijit Singh Music Collection")
    arijit_label.pack(pady=20)

    link1_button = tk.Button(arijit_window, text="Channa Mereya", command=lambda: open_link("https://drive.google.com/file/d/12cAh2CvNZ8-U7HJEA5wvSIknvY-tQr04/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(arijit_window, text="Har Kisi Ko", command=lambda: open_link("https://drive.google.com/file/d/1Ox0UJwUP6uFWbCwiWbFos1AFOLBa-VSa/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(arijit_window, text="Kabira", command=lambda: open_link("https://drive.google.com/file/d/1gYeSFHJdpSnbP2LzBpjBmtEIEIvVYyS0/view?usp=drive_linka"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(arijit_window, text="O Bedardeya", command=lambda: open_link("https://drive.google.com/file/d/1u91SlsxxaqVOfeLbE8ARuoqn0uVR_tc1/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(arijit_window, text="Pachtaoge", command=lambda: open_link("https://drive.google.com/file/d/16SzNirlm_YFEF-B0QqBHM9_3aXK4k6xa/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(arijit_window, text="Pyaar Hona Kayi Baar Hai", command=lambda: open_link("https://drive.google.com/file/d/13GCqz_MtJCW3uvMYTsCOvNXDz5zZTtJ7/view?usp=drive_linka"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(arijit_window, text="Raabta", command=lambda: open_link("https://drive.google.com/file/d/16gx_KvdmLOXLihk68ltRGB96hwIT2Yuo/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(arijit_window, text="Soulmate", command=lambda: open_link("https://drive.google.com/file/d/177PIkAYadkgVIM1ZE7MVVBTHz0wWWOsF/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(arijit_window, text="Tera Ban Jaunga", command=lambda: open_link("https://drive.google.com/file/d/1BX7TIQy5c0D5kT_UYknmEFAksAmx9kIW/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(arijit_window, text="Tum Hi Ho", command=lambda: open_link("https://drive.google.com/file/d/1modZSrXfxQUNi6fAvCNKtzBhotQpqK3_/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(arijit_window, text="Back to Home", command=lambda: return_to_home(arijit_window)).pack(pady=10)

    arijit_window.mainloop()

def open_kk_page(hindi_window):
    hindi_window.withdraw()
    
    kk_window = tk.Tk()
    kk_window.title("KK Library")
    
    kk_label = tk.Label(kk_window, text="KK Music Collection")
    kk_label.pack(pady=20)

    link1_button = tk.Button(kk_window, text="Ankhon Mein Teri", command=lambda: open_link("https://drive.google.com/file/d/1jABec6OvZoJVOYOdBAqaZCuwZViTGKtt/view?usp=drive_linka"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(kk_window, text="Dil Ibaadat", command=lambda: open_link("https://drive.google.com/file/d/1Qtyt6Slas56AIXwYEYw1FpdpHLTaerxr/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(kk_window, text="Dil Kyun Yeh Mera", command=lambda: open_link("https://drive.google.com/file/d/13eO0pyzzETgHQWYlY-f-nV2z2kQWzYaq/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(kk_window, text="Hasi", command=lambda: open_link("https://drive.google.com/file/d/1pjhs4-CjIF5eD4x1msYYJ9aCcaRfZnrw/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(kk_window, text="Khuda Jaane", command=lambda: open_link("https://drive.google.com/file/d/1__Ac73m24Wq6EJy9d4AqJSccUUa-geV6/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(kk_window, text="Make Some Noise For the Desi Boyz", command=lambda: open_link("https://drive.google.com/file/d/1LDUeywI0jTTRFFwJbJvscQLHAFC7zgqK/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(kk_window, text="Pyaar Ke Pal", command=lambda: open_link("https://drive.google.com/file/d/1oqhz9bSZA8Zalc4KAjg8GjgFvkRe5B9s/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(kk_window, text="Tadap Tadap", command=lambda: open_link("https://drive.google.com/file/d/1qVwJxi3ElhYZrA0KTrmmBhsmUOkaP2cy/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(kk_window, text="Yaaron", command=lambda: open_link("https://drive.google.com/file/d/1qVwJxi3ElhYZrA0KTrmmBhsmUOkaP2cy/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(kk_window, text="Zindagi Do Pal Ki", command=lambda: open_link("https://drive.google.com/file/d/1eRs9mPNTuosKO8XvPdjQsfxVnAU2b4xw/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(kk_window, text="Back to Home", command=lambda: return_to_home(kk_window)).pack(pady=10)

    kk_window.mainloop()

def open_pritam_chakraborty_page(hindi_window):
    hindi_window.withdraw()
    
    pritam_window = tk.Tk()
    pritam_window.title("Pritam Chakraborty Library")
    
    pritam_label = tk.Label(pritam_window, text="Pritam Chakraborty Music Collection")
    pritam_label.pack(pady=20)

    link1_button = tk.Button(pritam_window, text="Aahun Aahun", command=lambda: open_link("https://drive.google.com/file/d/1GTVFAfUvYr5_rRKxfJQ-H3ovz4P-obXh/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(pritam_window, text="Ajj Din Chadheya", command=lambda: open_link("https://drive.google.com/file/d/1VadMag1iVzVFk_062e77c46zx2dpKjN7/view?usp=drive_linka"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(pritam_window, text="Baarish", command=lambda: open_link("https://drive.google.com/file/d/1m8r646_ra7zqgEQQZpJppULqmjdC1U0L/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(pritam_window, text="Channa Mereya", command=lambda: open_link("https://drive.google.com/file/d/1fNoh6_IpYVWEx0RI4NZjBGUNrNX0Couu/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(pritam_window, text="Chor Bazaari", command=lambda: open_link("https://drive.google.com/file/d/1DDKOwXesLIpjQMyC1yVRlsjl6FvwtiLF/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(pritam_window, text="Kabira", command=lambda: open_link("https://drive.google.com/file/d/1RSZHIh1FAfzoarN-kTHwCslc3hYXdge6/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(pritam_window, text="Pee Loon", command=lambda: open_link("https://drive.google.com/file/d/1yoHB-CLVSV3dHWbNBbjV4uv24z2DO2gK/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(pritam_window, text="Subha Hone Na De", command=lambda: open_link("https://drive.google.com/file/d/1gfjPRO4J4mlexQwDhCcuQCtpaiiAznUW/view?usp=drive_linka"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(pritam_window, text="Tum Hi Ho Bandhu", command=lambda: open_link("https://drive.google.com/file/d/1aUbgGZ_36SsSutE9jeR2QIMjCRsMPIFp/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(pritam_window, text="Zindagi Do Pal Ki", command=lambda: open_link("https://drive.google.com/file/d/1RKMeZMBGGpGi4hUqNe2JWQoJuXK7smTG/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(pritam_window, text="Back to Home", command=lambda: return_to_home(pritam_window)).pack(pady=10)

    pritam_window.mainloop()

def open_sanam_page(hindi_window):
    hindi_window.withdraw()
    
    sanam_window = tk.Tk()
    sanam_window.title("SANAM Library")
    
    sanam_label = tk.Label(sanam_window, text="SANAM Music Collection")
    sanam_label.pack(pady=20)

    link1_button = tk.Button(sanam_window, text="Aap Ki Nazron Ne Samjha", command=lambda: open_link("https://drive.google.com/file/d/1YfKUJShHtJ6cpTwx4HsR_uKA4nUvGhgP/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(sanam_window, text="Ek Ladki Ko Dekha To", command=lambda: open_link("https://drive.google.com/file/d/1jKQVYS3EP0mCncaekA1lXjDDCmxEHZ_O/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(sanam_window, text="Gulabi Aankhen", command=lambda: open_link("https://drive.google.com/file/d/14j4oC2u5HuilMg9OajlHldf8ZGnKTBYw/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(sanam_window, text="Hai Apna Dil To Awara", command=lambda: open_link("https://drive.google.com/file/d/1Cf82U8T-eU3fay_CxvBq6q2V0gT7Nf7f/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(sanam_window, text="Lag Jaa Gale", command=lambda: open_link("https://drive.google.com/file/d/1LYqpdrDTmWOdOHVBp9-cZvdzue4Y1zqG/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(sanam_window, text="Mere Mehboob Qayamat Hogi", command=lambda: open_link("https://drive.google.com/file/d/1fEprdf4xw-H95H1U74idPYD_OGbYDi39/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(sanam_window, text="O Mere Dil Ke Chain", command=lambda: open_link("https://drive.google.com/file/d/1vufBvo8k5rVfd-vAM_-KugnQZbfB1C-p/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(sanam_window, text="Pehla Nasha", command=lambda: open_link("https://drive.google.com/file/d/1aSStaHVOnooeeV2kXTT2Vic3X2587QD8/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(sanam_window, text="Tujhse Naraz Nahi Zindagi", command=lambda: open_link("https://drive.google.com/file/d/127USEtoaw3a70ek08a2tFvOpnoGXECz3/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(sanam_window, text="Yeh Raaten Yeh Mausam", command=lambda: open_link("https://drive.google.com/file/d/18h4xNXW5PqfoId57w4hreA3D6qrQfer7/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(sanam_window, text="Back to Home", command=lambda: return_to_home(sanam_window)).pack(pady=10)

    sanam_window.mainloop()

def open_hindi_page():
    root.withdraw()
    
    hindi_window = tk.Tk()
    hindi_window.title("Hindi Music Library")
    
    hindi_label = tk.Label(hindi_window, text="Welcome to the Hindi Music Library!")
    hindi_label.pack(pady=20)

    ar_rahman_button = tk.Button(hindi_window, text="AR Rahman", command=lambda: open_ar_rahman_page(hindi_window))
    ar_rahman_button.pack(pady=10)

    arijit_singh_button = tk.Button(hindi_window, text="Arijit Singh", command=lambda: open_arijit_singh_page(hindi_window))
    arijit_singh_button.pack(pady=10)
    
    kk_button = tk.Button(hindi_window, text="KK", command=lambda: open_kk_page(hindi_window))
    kk_button.pack(pady=10)

    pritam_chakraborty_button = tk.Button(hindi_window, text="Pritam Chakraborty", command=lambda: open_pritam_chakraborty_page(hindi_window))
    pritam_chakraborty_button.pack(pady=10)

    sanam_button = tk.Button(hindi_window, text="SANAM", command=lambda: open_sanam_page(hindi_window))
    sanam_button.pack(pady=10)
    
    back_button = tk.Button(hindi_window, text="Back to Home", command=lambda: return_to_home(hindi_window))
    back_button.pack(pady=10)
    
    hindi_window.mainloop()

def open_ap_dhillon_page(punjabi_window):
    punjabi_window.withdraw()
    
    ap_dhillon_window = tk.Tk()
    ap_dhillon_window.title("AP Dhillon Library")
    
    ap_dhillon_label = tk.Label(ap_dhillon_window, text="AP Dhillon Music Collection")
    ap_dhillon_label.pack(pady=20)

    link1_button = tk.Button(ap_dhillon_window, text="Arrogant", command=lambda: open_link("https://drive.google.com/file/d/1ovRnckFAKAzQpHBr8azv4ofpSy2c2wIo/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(ap_dhillon_window, text="Brown Munde", command=lambda: open_link("https://drive.google.com/file/d/121c36bhT0MvWFy1kyJ1ErRGH73qYfxZ_/view?usp=drive_linka"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(ap_dhillon_window, text="Excuses", command=lambda: open_link("https://drive.google.com/file/d/1AcrAKM9k2Xmzfga1nqLmST1dCQdfFiUJ/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(ap_dhillon_window, text="Final Thoughts", command=lambda: open_link("https://drive.google.com/file/d/1SbZwud2h2k8Ors_MbmOCcO8V7EDI06HM/view?usp=drive_linka"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(ap_dhillon_window, text="Saada Pyaar", command=lambda: open_link("https://drive.google.com/file/d/16qo1a3_iOfu5uRrYwaeqSKagbELJuDb8/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(ap_dhillon_window, text="Sleepless", command=lambda: open_link("https://drive.google.com/file/d/1aNOY-syIxGDzlf-7e-tzYou22a7gp_uw/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(ap_dhillon_window, text="Summer High", command=lambda: open_link("https://drive.google.com/file/d/1coruAOyy1Wr_t2NwRhHroZecMCen9wL5/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(ap_dhillon_window, text="Toxic", command=lambda: open_link("https://drive.google.com/file/d/1iEC8uCeRDbqi0ZnYjxxAJeLSXAaR_EdX/view?usp=drive_linka"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(ap_dhillon_window, text="True Stories", command=lambda: open_link("https://drive.google.com/file/d/1xnzCPaNKi_Ualz9bfWHBoLi0Uy7BJrrK/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(ap_dhillon_window, text="With You", command=lambda: open_link("https://drive.google.com/file/d/1ZO02qpXhtGlwTUzQwCJfIJnbLsja-Z-l/view?usp=drive_link"))
    link10_button.pack(pady=10)
    
    tk.Button(ap_dhillon_window, text="Back to Home", command=lambda: return_to_home(ap_dhillon_window)).pack(pady=10)

    ap_dhillon_window.mainloop()

def open_diljit_dosanjh_page(punjabi_window):
    punjabi_window.withdraw()
    
    diljit_dosanjh_window = tk.Tk()
    diljit_dosanjh_window.title("Diljit Dosanjh Library")
    
    diljit_dosanjh_label = tk.Label(diljit_dosanjh_window, text="Diljit Dosanjh Music Collection")
    diljit_dosanjh_label.pack(pady=20)

    link1_button = tk.Button(diljit_dosanjh_window, text="Born To Shine", command=lambda: open_link("https://drive.google.com/file/d/1yLXXqsZlINthn7tL1298QPe_rVrL0zJO/view?usp=drive_linka"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(diljit_dosanjh_window, text="Do You Know", command=lambda: open_link("https://drive.google.com/file/d/1MikuYl9PO5z1mCVTgHpGmmVreCjNLsqn/view?usp=drive_linka"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(diljit_dosanjh_window, text="G.O.A.T.", command=lambda: open_link("https://drive.google.com/file/d/1T_S9baYU94OjADr1sjTV2VJalUjkBYD7/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(diljit_dosanjh_window, text="Hass Hass", command=lambda: open_link("https://drive.google.com/file/d/1Kr51CxYfaY9sHwxOCSpFSAjWCnWlGzrP/view?usp=drive_linka"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(diljit_dosanjh_window, text="Kinni Kinni", command=lambda: open_link("https://drive.google.com/file/d/1DWQ1SpahuQeQfOqeXT8TIhkaIrO_4jc_/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(diljit_dosanjh_window, text="Lalkara", command=lambda: open_link("https://drive.google.com/file/d/1EdaAC1W3G6hYmBopG4JwjQJYepkOKOcB/view?usp=drive_linka"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(diljit_dosanjh_window, text="Lover", command=lambda: open_link("https://drive.google.com/file/d/1lR0PqRugYx5fHCLGdCl0EuoHIcux8ZD4/view?usp=drive_linka"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(diljit_dosanjh_window, text="Magic", command=lambda: open_link("https://drive.google.com/file/d/1xUkE3P_VKJDoG5-Ce3Ekpv5dcght9SKb/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(diljit_dosanjh_window, text="Patiala Peg", command=lambda: open_link("https://drive.google.com/file/d/1F4ESYJSp6QsHi-6Tm1F303-BiqyIy8x2/view?usp=drive_linka"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(diljit_dosanjh_window, text="Sauda Khara Khara", command=lambda: open_link("https://drive.google.com/file/d/1S9szPoH1_I7bekXPSbD0SqqJahUGQZX9/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(diljit_dosanjh_window, text="Back to Home", command=lambda: return_to_home(diljit_dosanjh_window)).pack(pady=10)

    diljit_dosanjh_window.mainloop()

def open_karan_aujla_page(punjabi_window):
    punjabi_window.withdraw()
    
    karan_aujla_window = tk.Tk()
    karan_aujla_window.title("Karan Aujla Library")
    
    karan_aujla_label = tk.Label(karan_aujla_window, text="Karan Aujla Music Collection")
    karan_aujla_label.pack(pady=20)

    link1_button = tk.Button(karan_aujla_window, text="52 Bars", command=lambda: open_link("https://drive.google.com/file/d/1oa5H_mqSDMj8Mrr8IQE6-LATDlW4k6gr/view?usp=drive_linka"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(karan_aujla_window, text="Admirin' You", command=lambda: open_link("https://drive.google.com/file/d/1FBCcNuDUD24P_pltYDd1WXv8jIhONg53/view?usp=drive_linka"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(karan_aujla_window, text="Bachke Bachke", command=lambda: open_link("https://drive.google.com/file/d/1RqqkN1u5lSQpmw--KY2y2cRTLm6pXNQK/view?usp=drive_linka"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(karan_aujla_window, text="Chitta Kurta", command=lambda: open_link("https://drive.google.com/file/d/1M4DKsZLt5Q74Idy1ayT9FGzwalK0Orjc/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(karan_aujla_window, text="Jee Ni Lagda", command=lambda: open_link("https://drive.google.com/file/d/1H24j9t-GNLX7vlEGmWeDYWyVJ-PQHQ_U/view?usp=drive_linka"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(karan_aujla_window, text="Players", command=lambda: open_link("https://drive.google.com/file/d/1H24j9t-GNLX7vlEGmWeDYWyVJ-PQHQ_U/view?usp=drive_linka"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(karan_aujla_window, text="Softly", command=lambda: open_link("https://drive.google.com/file/d/1BNl-pVOR-ScZMjXA40GPe1w5sIRIZxfv/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(karan_aujla_window, text="Tauba Tauba", command=lambda: open_link("https://drive.google.com/file/d/1juPYpbWg87AkcuNrNrqii7fDKIootFuP/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(karan_aujla_window, text="White Brown Black", command=lambda: open_link("https://drive.google.com/file/d/1-15b_9V3_rFJMYUzXU3pUK0tm73sQU_l/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(karan_aujla_window, text="Winnign Speech", command=lambda: open_link("https://drive.google.com/file/d/1ckl7bX5xZ-Jlk-nNx1R_ErCDJyN8J0c6/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(karan_aujla_window, text="Back to Home", command=lambda: return_to_home(karan_aujla_window)).pack(pady=10)

    karan_aujla_window.mainloop()

def open_rabbi_shergill_page(punjabi_window):
    punjabi_window.withdraw()
    
    rabbi_shergill_window = tk.Tk()
    rabbi_shergill_window.title("Rabbi Shergill Library")
    
    rabbi_shergill_label = tk.Label(rabbi_shergill_window, text="Rabbi Shergill Music Collection")
    rabbi_shergill_label.pack(pady=20)

    link1_button = tk.Button(rabbi_shergill_window, text="Bandiya Tu", command=lambda: open_link("https://drive.google.com/file/d/1vKwAru-Y9JdWMW_83m-n4YGCo83q5Uwj/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(rabbi_shergill_window, text="Bulla Ki Jaana Main Kaun", command=lambda: open_link("https://drive.google.com/file/d/1a06ZLz_nJgAs5L0Wv8GjpH2Vpl5PN5qI/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(rabbi_shergill_window, text="Bulleya", command=lambda: open_link("https://drive.google.com/file/d/1mLToBHfdFfjTfs1QfLdNBct6ou6YQqTz/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(rabbi_shergill_window, text="Challa", command=lambda: open_link("https://drive.google.com/file/d/1WLMzUNI6nSgv3XKMyIHNnS01UKaQbEC1/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(rabbi_shergill_window, text="Gil Te Guitar", command=lambda: open_link("https://drive.google.com/file/d/1_bKvdYzrT-EfxOUZ_VGafd9Hxqmv-CGL/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(rabbi_shergill_window, text="Ishtihar", command=lambda: open_link("https://drive.google.com/file/d/1ajLBQ7omSTrK2ffmmD1SRmmCuCXRSJ5U/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(rabbi_shergill_window, text="Jugni", command=lambda: open_link("https://drive.google.com/file/d/10pDBtdL1v4LaoC6BH66fKTicNMEbniNl/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(rabbi_shergill_window, text="Pahilan", command=lambda: open_link("https://drive.google.com/file/d/1JSxLicjkfoeM2n3hKtY1M9dAvFLhuF_q/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(rabbi_shergill_window, text="Tere Bin", command=lambda: open_link("https://drive.google.com/file/d/1_KPCjcNvWSkkRVaPAkM7Mz2vA1SxQD8O/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(rabbi_shergill_window, text="Totia Manmotia", command=lambda: open_link("https://drive.google.com/file/d/1LhEiQNm5ddc9g3YUgzZwkfFIg_goxEV1/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(rabbi_shergill_window, text="Back to Home", command=lambda: return_to_home(rabbi_shergill_window)).pack(pady=10)

    rabbi_shergill_window.mainloop()

def open_honey_singh_page(punjabi_window):
    punjabi_window.withdraw()

    honey_singh_window = tk.Tk()
    honey_singh_window.title("Yo Yo Honey Singh Library")

    honey_singh_label = tk.Label(honey_singh_window, text="Yo Yo Honey Singh Music Collection")
    honey_singh_label.pack(pady=20)

    link1_button = tk.Button(honey_singh_window, text="Alcoholic", command=lambda: open_link("https://drive.google.com/file/d/1pKMlOi4qLY8XQIfaXTs6zMskQRkxPrp5/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(honey_singh_window, text="Angreji Beat", command=lambda: open_link("https://drive.google.com/file/d/1ejuGZl-zcEpzIqC4TgvsR6jwR-3YtCmr/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(honey_singh_window, text="Brown Rang", command=lambda: open_link("https://drive.google.com/file/d/1tKvFk4A70_GP9OWWkLNvTDrTsnXtvHJV/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(honey_singh_window, text="Chaar Bottle Vodka", command=lambda: open_link("https://drive.google.com/file/d/1XQJIH-n7bUOwBf9mw1HPAHOZFTwhQQk0/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(honey_singh_window, text="Desi Kalakar", command=lambda: open_link("https://drive.google.com/file/d/1KVx3KKrSVWzK3-llMaMVROe-I3OSBAT9/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(honey_singh_window, text="Dope Shope", command=lambda: open_link("https://drive.google.com/file/d/1mCE4vkMhGm_SQDD5yOFO5SDasF5Mdtts/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(honey_singh_window, text="Khadke Glassy", command=lambda: open_link("https://drive.google.com/file/d/1kKqAcBPZb95usE8gR90TKAFoFJlTc-rZ/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(honey_singh_window, text="Love Dose", command=lambda: open_link("https://drive.google.com/file/d/1Ul6opdRNHlfYKICILctdaQN64l3IasPf/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(honey_singh_window, text="Manali Trance", command=lambda: open_link("https://drive.google.com/file/d/1gVzSN447bo0yHblEz5yTPZwC65v7PxZO/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(honey_singh_window, text="One Bottle Down", command=lambda: open_link("https://drive.google.com/file/d/1mTH86dOOnyANM_FCW2QtTee1KtIvNDuy/view?usp=drive_linka"))
    link10_button.pack(pady=10)

    tk.Button(honey_singh_window, text="Back to Home", command=lambda: return_to_home(honey_singh_window)).pack(pady=10)

    honey_singh_window.mainloop()

def open_punjabi_page():
    root.withdraw()
    
    punjabi_window = tk.Tk()
    punjabi_window.title("Punjabi Music Library")
    
    punjabi_label = tk.Label(punjabi_window, text="Welcome to the Punjabi Music Library!")
    punjabi_label.pack(pady=20)
    
    ap_dhillon_button = tk.Button(punjabi_window, text="AP Dhillon", command=lambda: open_ap_dhillon_page(punjabi_window))
    ap_dhillon_button.pack(pady=10)

    diljit_dosanjh_button = tk.Button(punjabi_window, text="Diljit Dosanjh", command=lambda: open_diljit_dosanjh_page(punjabi_window))
    diljit_dosanjh_button.pack(pady=10)
    
    karan_aujla_button = tk.Button(punjabi_window, text="Karan Aujla", command=lambda: open_karan_aujla_page(punjabi_window))
    karan_aujla_button.pack(pady=10)

    rabbi_shergill_button = tk.Button(punjabi_window, text="Rabbi Shergill", command=lambda: open_rabbi_shergill_page(punjabi_window))
    rabbi_shergill_button.pack(pady=10)

    honey_singh_button = tk.Button(punjabi_window, text="Yo Yo Honey Singh", command=lambda: open_honey_singh_page(punjabi_window))
    honey_singh_button.pack(pady=10)

    back_button = tk.Button(punjabi_window, text="Back to Home", command=lambda: return_to_home(punjabi_window))
    back_button.pack(pady=10)
    
    punjabi_window.mainloop()

def open_ali_sethi_page(urdu_window):
    urdu_window.withdraw()
    
    ali_sethi_window = tk.Tk()
    ali_sethi_window.title("Ali Sethi Library")
    
    ali_sethi_label = tk.Label(ali_sethi_window, text="Ali Sethi Music Collection")
    ali_sethi_label.pack(pady=20)

    link1_button = tk.Button(ali_sethi_window, text="Aaqa Abida", command=lambda: open_link("https://drive.google.com/file/d/1CD3wBoLAkkcp-Vlk1Vb_3opPF5r6GzuR/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(ali_sethi_window, text="Chan Kithan", command=lambda: open_link("https://drive.google.com/file/d/1BTHr-z1fRwFQQLjQ3o1cW_nGx1UrOJAM/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(ali_sethi_window, text="Dil Ki Khair", command=lambda: open_link("https://drive.google.com/file/d/1BTHr-z1fRwFQQLjQ3o1cW_nGx1UrOJAM/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(ali_sethi_window, text="Ghazab Kiya", command=lambda: open_link("https://drive.google.com/file/d/1jC3y1O8y4iN9m9Lb5Ugp2GidfJNPUMOQ/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(ali_sethi_window, text="Gulon Mein Rang", command=lambda: open_link("https://drive.google.com/file/d/1cElPrnEPDoVizOyNjolJKTbatrXI63w5/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link9_button = tk.Button(ali_sethi_window, text="Honthon Pe Bas", command=lambda: open_link("https://drive.google.com/file/d/1apxUDnG-tLmZdKjCcYCokBYOdsijsW3j/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link6_button = tk.Button(ali_sethi_window, text="Mere Aur Hein Iraaday", command=lambda: open_link("https://drive.google.com/file/d/1-Oq5uGOps1GoOrU-F_KW9KAeRO3JOWnw/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(ali_sethi_window, text="Pasoori", command=lambda: open_link("https://drive.google.com/file/d/1c3WSnyxw-ozE2Wtw5rIbcUDl-P3ghaqg/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(ali_sethi_window, text="Rung", command=lambda: open_link("https://drive.google.com/file/d/1YdlhrCZw5MPtqJsod0kCNfMf811QSltI/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link10_button = tk.Button(ali_sethi_window, text="Zindagi Hai Ajnabi", command=lambda: open_link("https://drive.google.com/file/d/1EYxXuBWTv0Tcp3l6sN7auADxgWInWgiE/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(ali_sethi_window, text="Back to Home", command=lambda: return_to_home(ali_sethi_window)).pack(pady=10)

    ali_sethi_window.mainloop()

def open_atif_aslam_page(urdu_window):
    urdu_window.withdraw()
    
    atif_aslim_window = tk.Tk()
    atif_aslim_window.title("Atif Aslim Library")
    
    atif_aslim_label = tk.Label(atif_aslim_window, text="Atif Aslim Music Collection")
    atif_aslim_label.pack(pady=20)

    link1_button = tk.Button(atif_aslim_window, text="Baarish", command=lambda: open_link("https://drive.google.com/file/d/1pAIdrZv4fE1jnA5Z0-grtteIAV7hxPGS/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(atif_aslim_window, text="Dil Meri Na Sune", command=lambda: open_link("https://drive.google.com/file/d/1upMajfS8VMX45uQDlvEk2TUmQ1sVozvn/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(atif_aslim_window, text="Jeena Jeena", command=lambda: open_link("https://drive.google.com/file/d/1ysyntaxp6p4I68FZSRZ2gst_3qGiZjNt/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(atif_aslim_window, text="Jab Koi Baat", command=lambda: open_link("https://drive.google.com/file/d/11WbNfPAAzfwV0Ootqlc0075lzMp_9J9t/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(atif_aslim_window, text="Khair Mangda", command=lambda: open_link("https://drive.google.com/file/d/1q5LN6QFhPtHlo_I9rDD-becveN7LEEim/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(atif_aslim_window, text="O Saathi", command=lambda: open_link("https://drive.google.com/file/d/16zbR6NG1WLe_4vjmbR8KNfwPeld2chFx/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(atif_aslim_window, text="Tera Hua", command=lambda: open_link("https://drive.google.com/file/d/11F0UUt8aq73fZvEYjg8OZOvMPHUNA7C7/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(atif_aslim_window, text="Tere Sang Yaara", command=lambda: open_link("https://drive.google.com/file/d/1OSxfVwF-KndE7vFRaw_nlGIvmljPqa2A/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(atif_aslim_window, text="Tu Jaane Na", command=lambda: open_link("https://drive.google.com/file/d/1Uj6cNsyCNewI_pPJL6tqfmSWW9UoGKKT/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(atif_aslim_window, text="Woh Lamhe Woh Baatein", command=lambda: open_link("https://drive.google.com/file/d/1n_dMZME1y2_91zCvpkIeS8S2FvgTACB0/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(atif_aslim_window, text="Back to Home", command=lambda: return_to_home(atif_aslim_window)).pack(pady=10)

    atif_aslim_window.mainloop()

def open_aur_page(urdu_window):
    urdu_window.withdraw()
    
    aur_window = tk.Tk()
    aur_window.title("AUR Library")
    
    aur_label = tk.Label(aur_window, text="AUR Music Collection")
    aur_label.pack(pady=20)

    link6_button = tk.Button(aur_window, text="Aaja Mahi", command=lambda: open_link("https://drive.google.com/file/d/1qeb6ud6WTGypOLBBaBMoWkDjNOyjsP8u/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link1_button = tk.Button(aur_window, text="Chal Diye Tum Kahan", command=lambda: open_link("https://drive.google.com/file/d/1v4CNSOsBUQYX5POm-G7udUaLkyizqCCw/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(aur_window, text="Dooriyan", command=lambda: open_link("https://drive.google.com/file/d/1dE8W2ZIgm6kVb_Nv_kg1gZypDRp3xhIv/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link9_button = tk.Button(aur_window, text="Kabhi Mein Kabhi Tum2", command=lambda: open_link("https://drive.google.com/file/d/1pKcII5nQtL83VAPDX4p0EwQh2ID_gw3H/view?usp=drive_link"))
    link9_button.pack(pady=10)
    
    link3_button = tk.Button(aur_window, text="Kya Chahiye", command=lambda: open_link("https://drive.google.com/file/d/1Avf0hQevqRrIcwh0m4DP2XIWxKu0vC1F/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(aur_window, text="Never", command=lambda: open_link("https://drive.google.com/file/d/1wqn8mVaknkzG11UgGCuaUFRAfaIeZ3HC/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(aur_window, text="No Way To Nowhere", command=lambda: open_link("https://drive.google.com/file/d/1XQEUYy6k9K4JzdeCefF7MkI-KKX8YtwM/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link7_button = tk.Button(aur_window, text="Shikayat", command=lambda: open_link("https://drive.google.com/file/d/1YDmz09uwYfIzeFCOqNLpQWL5poIuRN8-/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(aur_window, text="Sometimes", command=lambda: open_link("https://drive.google.com/file/d/1j6rVZR0JeOCzUDRwJHQSp8Ic642i-LqN/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link10_button = tk.Button(aur_window, text="Tu Hai Kahan", command=lambda: open_link("https://drive.google.com/file/d/1Q3CD_cbKKXJl0EB_9tqtFO7ez7OOJExh/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(aur_window, text="Back to Home", command=lambda: return_to_home(aur_window)).pack(pady=10)

    aur_window.mainloop()

def open_nusrat_page(urdu_window):
    urdu_window.withdraw()
    
    nusrat_window = tk.Tk()
    nusrat_window.title("Nusrat Fatef Ali Khan Library")
    
    nusrat_label = tk.Label(nusrat_window, text="Nusrat Fateh Ali Khan Music Collection")
    nusrat_label.pack(pady=20)

    link1_button = tk.Button(nusrat_window, text="Aankh Uthi Mohabbat Ne", command=lambda: open_link("https://drive.google.com/file/d/17eEAQpQfRcRmAAHCLPq8Omj8QExCzBFC/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(nusrat_window, text="Afreen Afreen", command=lambda: open_link("https://drive.google.com/file/d/17eWeQtYVhd_gAEYy4ETki4IpRoZiJS6O/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(nusrat_window, text="Ghaus Ul Azam Sha e Jilani", command=lambda: open_link("https://drive.google.com/file/d/17cmxqVxQePmF7WUXU3T3JDrpLe4jp7k7/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(nusrat_window, text="Jhoom Jhoom Jhoom Baba", command=lambda: open_link("https://drive.google.com/file/d/17ZFycV3J2mOZUYCC7WTGCSdMZys1ru1O/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(nusrat_window, text="Kaisa Yeh Pyaar Hai Allah Allah", command=lambda: open_link("https://drive.google.com/file/d/17dVCNXBqm-5Zq6GVDYRZe1kw3cmmjxPJ/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(nusrat_window, text="Kali Kali Zulfon Ke Phande Na", command=lambda: open_link("https://drive.google.com/file/d/17d0JK0n1cgWtjhqsGMg3EJA1KfbdsUcM/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(nusrat_window, text="Kinna Sohna Tenu Rab Ne Banaya", command=lambda: open_link("https://drive.google.com/file/d/17Z9CdHl02jhM9NNUx5ouugtFcXLhkdeo/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(nusrat_window, text="Mera Piya Ghar Aaya", command=lambda: open_link("https://drive.google.com/file/d/17P5S8-oaRtRMYsJTaKpolTT-x5lkvSJe/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(nusrat_window, text="Tajdar-e-Haram", command=lambda: open_link("https://drive.google.com/file/d/17FKugdV_ziP-dzikySoPenhuvGNZSvMk/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(nusrat_window, text="Tumhein Dilagi Bhool Jaani Paray Gi", command=lambda: open_link("https://drive.google.com/file/d/17Ht-uw9ETpo9o7ri4uJ50fKpquXAtLy4/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(nusrat_window, text="Back to Home", command=lambda: return_to_home(nusrat_window)).pack(pady=10)

    nusrat_window.mainloop()

def open_shae_gill_page(urdu_window):
    urdu_window.withdraw()
    
    shae_gill_window = tk.Tk()
    shae_gill_window.title("Shae Gill Library")
    
    shae_gill_label = tk.Label(shae_gill_window, text="Shae Gill Music Collection")
    shae_gill_label.pack(pady=20)

    link1_button = tk.Button(shae_gill_window, text="Bulleya", command=lambda: open_link("https://drive.google.com/file/d/16siiAumPxZE3beQ3JLtnfTnUs8VGjKLx/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(shae_gill_window, text="Dil-E-Veeran", command=lambda: open_link("https://drive.google.com/file/d/15voo5QtZo_lmxTbvouC7nUa5X7tPN8qo/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(shae_gill_window, text="Gulabi Ankheyn", command=lambda: open_link("https://drive.google.com/file/d/16k2D3UWwW6D2-P0QOOEboFlneqaFSYYA/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(shae_gill_window, text="Left Right", command=lambda: open_link("https://drive.google.com/file/d/16vF7WUDKSRyOHoY2EKMp5SEJ7blwLSi8/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(shae_gill_window, text="Mera Sawera", command=lambda: open_link("https://drive.google.com/file/d/171lZA15uHA3u8zj7k10dskBI_i2aTwn4/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(shae_gill_window, text="One Love", command=lambda: open_link("https://drive.google.com/file/d/17-nrlBNkoiIOMoz1WUVuBcQJUSo_xayS/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(shae_gill_window, text="Pasoori", command=lambda: open_link("https://drive.google.com/file/d/16pc0LnXjJJC8Lf-7w7JqiBrMqeiuE5hW/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(shae_gill_window, text="Sab Sitaray Humaray", command=lambda: open_link("https://drive.google.com/file/d/1ZY65MnX0z1N66anxH-q3lNjur2UI1MJR/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(shae_gill_window, text="Sukoon", command=lambda: open_link("https://drive.google.com/file/d/16tapP6ocUG-X3QNVNc5-tY1bx2sim0-0/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(shae_gill_window, text="Wo Humsafar Tha", command=lambda: open_link("https://drive.google.com/file/d/16hjflT8EUhSY8dBJKSGKb2j42hz71q0b/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(shae_gill_window, text="Back to Home", command=lambda: return_to_home(shae_gill_window)).pack(pady=10)

    shae_gill_window.mainloop()

def open_urdu_page():
    root.withdraw()
    
    urdu_window = tk.Tk()
    urdu_window.title("Urdu Music Library")
    
    urdu_label = tk.Label(urdu_window, text="Welcome to the Urdu Music Library!")
    urdu_label.pack(pady=20)
    
    ali_sethi_button = tk.Button(urdu_window, text="Ali Sethi", command=lambda: open_ali_sethi_page(urdu_window))
    ali_sethi_button.pack(pady=10)

    atif_aslam_button = tk.Button(urdu_window, text="Atif Aslam", command=lambda: open_atif_aslam_page(urdu_window))
    atif_aslam_button.pack(pady=10)
    
    aur_button = tk.Button(urdu_window, text="AUR", command=lambda: open_aur_page(urdu_window))
    aur_button.pack(pady=10)

    nusrat_button = tk.Button(urdu_window, text="Nusrat Fateh Ali Khan", command=lambda: open_nusrat_page(urdu_window))
    nusrat_button.pack(pady=10)

    shae_gill_button = tk.Button(urdu_window, text="Shae Gill", command=lambda: open_shae_gill_page(urdu_window))
    shae_gill_button.pack(pady=10)

    back_button = tk.Button(urdu_window, text="Back to Home", command=lambda: return_to_home(urdu_window))
    back_button.pack(pady=10)
    
    urdu_window.mainloop()

def open_charlie_puth_page(english_window):
    english_window.withdraw()
    
    charlie_puth_window = tk.Tk()
    charlie_puth_window.title("Charlie Puth Library")
    
    charlie_puth_label = tk.Label(charlie_puth_window, text="Charlie Puth Music Collection")
    charlie_puth_label.pack(pady=20)

    link1_button = tk.Button(charlie_puth_window, text="Attention", command=lambda: open_link("https://drive.google.com/file/d/155XooMDEkFDRc5A-ZGwr5yZoJiXZGKRn/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(charlie_puth_window, text="Done For Me", command=lambda: open_link("https://drive.google.com/file/d/13q1Yfs02YFLauTS8VDv_u_CFUwdxw9LH/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(charlie_puth_window, text="How Long", command=lambda: open_link("https://drive.google.com/file/d/13lAmRFUWyFJCKMaraMUyQEZ9vxsCBtQt/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(charlie_puth_window, text="Light Switch", command=lambda: open_link("https://drive.google.com/file/d/13ioRfvgysWzxY3gGNTRXHOobrdE_yqYw/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(charlie_puth_window, text="Marvin Gaye", command=lambda: open_link("https://drive.google.com/file/d/12XAupwMY1GMEbT5is2WShQjywbyQdt-S/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(charlie_puth_window, text="One Call Away", command=lambda: open_link("https://drive.google.com/file/d/12W079jUenm0tdmHf7Pdatw0Bst5UvJqF/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(charlie_puth_window, text="See You Again", command=lambda: open_link("https://drive.google.com/file/d/12US0XlbR1UNBGOt54kdxMnJcideA5kPk/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(charlie_puth_window, text="The Way I Am", command=lambda: open_link("https://drive.google.com/file/d/12URgKvCzMxiTS3uV1RL8vS24xJsByRC_/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(charlie_puth_window, text="We Don't Talk Anymore", command=lambda: open_link("https://drive.google.com/file/d/12Jzs0lLMqYcJlAI2RQMOjZaNKZl54YeQ/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(charlie_puth_window, text="When You're Sad I'm Sad", command=lambda: open_link("https://drive.google.com/file/d/12JzSAPcMR5ROkUbD2IVOeuzv9ulsGYPw/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(charlie_puth_window, text="Back to Home", command=lambda: return_to_home(charlie_puth_window)).pack(pady=10)

    charlie_puth_window.mainloop()

def open_dua_lipa_page(english_window):
    english_window.withdraw()
    
    dua_lipa_window = tk.Tk()
    dua_lipa_window.title("Dua Lipa Library")
    
    dua_lipa_label = tk.Label(dua_lipa_window, text="Dua Lipa Music Collection")
    dua_lipa_label.pack(pady=20)

    link1_button = tk.Button(dua_lipa_window, text="Break My Heart", command=lambda: open_link("https://drive.google.com/file/d/12zfB05nIZ_yyjBwIcyJLoCajx_gl8jxa/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(dua_lipa_window, text="Don't Start Now", command=lambda: open_link("https://drive.google.com/file/d/12yxpKfJRmutROEJodqyB48j0KEblxMaK/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(dua_lipa_window, text="Hallucinate", command=lambda: open_link("https://drive.google.com/file/d/12xMFs2_B3ZA8EbmY3SJhSEYCBCGRF41p/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(dua_lipa_window, text="IDGAF", command=lambda: open_link("https://drive.google.com/file/d/12vXoxOnbnKMPsTfCW3-serbiZ3jC8-bG/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(dua_lipa_window, text="Levitating", command=lambda: open_link("https://drive.google.com/file/d/12thvnnoti0LcRLvqA8ruewh_NMIjMk0g/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(dua_lipa_window, text="Love Again", command=lambda: open_link("https://drive.google.com/file/d/12oTM0gs6L6i27DemIhXe4qswuQUoaRc1/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(dua_lipa_window, text="New Rules", command=lambda: open_link("https://drive.google.com/file/d/12kBQjk6HgxUioxY3HRqCsfBrj2UMzr7W/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(dua_lipa_window, text="One Kiss", command=lambda: open_link("https://drive.google.com/file/d/12k4LMqLAgPo_7500Pv8kj0mKPWCcaAGj/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(dua_lipa_window, text="Physical", command=lambda: open_link("https://drive.google.com/file/d/12jnHz5Npk5KaJDrh4bCgFJ9_RZVng5BL/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(dua_lipa_window, text="We're Good", command=lambda: open_link("https://drive.google.com/file/d/12iu2RsS5WP-mzGD2VJn1TiW6CGp2rGQR/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(dua_lipa_window, text="Back to Home", command=lambda: return_to_home(dua_lipa_window)).pack(pady=10)

    dua_lipa_window.mainloop()

def open_ed_sheeran_page(english_window):
    english_window.withdraw()
    
    ed_sheeran_window = tk.Tk()
    ed_sheeran_window.title("Ed Sheeran Library")
    
    ed_sheeran_label = tk.Label(ed_sheeran_window, text="Ed Sheeran Music Collection")
    ed_sheeran_label.pack(pady=20)

    link1_button = tk.Button(ed_sheeran_window, text="Bad Habits", command=lambda: open_link("https://drive.google.com/file/d/15Ty1eEwwXQSl_tKjKbNT27jPxanEOHSR/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(ed_sheeran_window, text="Castle On The Hill", command=lambda: open_link("https://drive.google.com/file/d/15RYRVMbfiK78jr-TucEZPKR9vapEihQm/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(ed_sheeran_window, text="Galway Girl", command=lambda: open_link("https://drive.google.com/file/d/15QZ2bv3E9XFhkowLfiA_SLy_3go3ckQt/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(ed_sheeran_window, text="I Don't Care", command=lambda: open_link("https://drive.google.com/file/d/13I8LTUG4aAEMmwpeA1b7Wy-ktTVF7JGk/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(ed_sheeran_window, text="Perfect", command=lambda: open_link("https://drive.google.com/file/d/13AB5_MxQSv0kq2M9hTHNtsloQ3oCoOS4/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(ed_sheeran_window, text="Photograph", command=lambda: open_link("https://drive.google.com/file/d/138HxREpVrPzcKrY2jHS2YZtDWBz5bbsN/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(ed_sheeran_window, text="Shivers", command=lambda: open_link("https://drive.google.com/file/d/133FaX0WyQqLFNqKrY3PJYkupJCEvhnbn/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(ed_sheeran_window, text="Shape Of You", command=lambda: open_link("https://drive.google.com/file/d/1371nOwuaI163G6zFjt3sHGDE5fw9dQDO/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(ed_sheeran_window, text="Thinking Out Loud", command=lambda: open_link("https://drive.google.com/file/d/130EO3m1OSPD1tjztCC_NRTSNgHc5nbfz/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(ed_sheeran_window, text="The A Team", command=lambda: open_link("https://drive.google.com/file/d/1311oOHeySRUhCv3gHNPPs734TiilNhe8/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(ed_sheeran_window, text="Back to Home", command=lambda: return_to_home(ed_sheeran_window)).pack(pady=10)

    ed_sheeran_window.mainloop()

def open_justin_bieber_page(english_window):
    english_window.withdraw()
    
    justin_bieber_window = tk.Tk()
    justin_bieber_window.title("Justin Bieber Library")
    
    justin_bieber_label = tk.Label(justin_bieber_window, text="Justin Bieber Music Collection")
    justin_bieber_label.pack(pady=20)

    link1_button = tk.Button(justin_bieber_window, text="Baby", command=lambda: open_link("https://drive.google.com/file/d/15zn7dHlSwgILl69dUe3CXpySXdi-3A3y/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(justin_bieber_window, text="Ghost", command=lambda: open_link("https://drive.google.com/file/d/15zkMzDHDQYFjeraV1dtLKU07h6lzQQSB/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(justin_bieber_window, text="Intentions", command=lambda: open_link("https://drive.google.com/file/d/15uCuJSrpIUoHWMqdP_D-HZ6yIV_8_XyN/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(justin_bieber_window, text="Let Me Love You", command=lambda: open_link("https://drive.google.com/file/d/15gjZN4FAR7nhQvQ9Azrm91cvOdPSGJTp/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(justin_bieber_window, text="Love Yourself", command=lambda: open_link("https://drive.google.com/file/d/15cFBEYBsg84IfAZs4wvXdjipzDvi6hM7/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(justin_bieber_window, text="Never Say Never", command=lambda: open_link("https://drive.google.com/file/d/15XztnO_-o7N86bonayDV-yiWTq6yS38o/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(justin_bieber_window, text="Peaches", command=lambda: open_link("https://drive.google.com/file/d/15UkY0gMRkuXWcSuIq50OI9MAb9DVxL8D/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(justin_bieber_window, text="Sorry", command=lambda: open_link("https://drive.google.com/file/d/14cvGfnyKbEGeOsqypFrBjaLm0cl1rDGE/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(justin_bieber_window, text="Stay", command=lambda: open_link("https://drive.google.com/file/d/14c98kAFRi0pMzgK8744Hhz6Cd-aXuBwB/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(justin_bieber_window, text="Yummy", command=lambda: open_link("https://drive.google.com/file/d/14aqDXe7GPqjnT0ECiih6p3USFfWtQtOh/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(justin_bieber_window, text="Back to Home", command=lambda: return_to_home(justin_bieber_window)).pack(pady=10)

    justin_bieber_window.mainloop()

def open_one_direction_page(english_window):
    english_window.withdraw()
    
    one_direction_window = tk.Tk()
    one_direction_window.title("One Direction Library")
    
    one_direction_label = tk.Label(one_direction_window, text="One Direction Music Collection")
    one_direction_label.pack(pady=20)

    link1_button = tk.Button(one_direction_window, text="Best Song Ever", command=lambda: open_link("https://drive.google.com/file/d/16Y5cAu4h2V-osQBfwWZYU_9Bp5OQU-rW/view?usp=drive_link"))
    link1_button.pack(pady=10)

    link2_button = tk.Button(one_direction_window, text="Drag Me Down", command=lambda: open_link("https://drive.google.com/file/d/16Tl0NyeYZt0q7g6116MnKOKJwNZKRB3W/view?usp=drive_link"))
    link2_button.pack(pady=10)

    link3_button = tk.Button(one_direction_window, text="History", command=lambda: open_link("https://drive.google.com/file/d/16TSOGs_Y_IYKFeTk6ufsCT-UmVuv-q36/view?usp=drive_link"))
    link3_button.pack(pady=10)

    link4_button = tk.Button(one_direction_window, text="Night Changes", command=lambda: open_link("https://drive.google.com/file/d/16TSOGs_Y_IYKFeTk6ufsCT-UmVuv-q36/view?usp=drive_link"))
    link4_button.pack(pady=10)

    link5_button = tk.Button(one_direction_window, text="Olivia", command=lambda: open_link("https://drive.google.com/file/d/16NCc3temTrq4zY3tH7AoOAEPwEkmGvQa/view?usp=drive_link"))
    link5_button.pack(pady=10)

    link6_button = tk.Button(one_direction_window, text="Perfect", command=lambda: open_link("https://drive.google.com/file/d/16NLiRL48PdtrYcwIfXdNAvNcqsL95xD9/view?usp=drive_link"))
    link6_button.pack(pady=10)

    link7_button = tk.Button(one_direction_window, text="Steal My Girl", command=lambda: open_link("https://drive.google.com/file/d/16EnDzdUVlvqb0ycTJRIYHvPfyvaoz-we/view?usp=drive_link"))
    link7_button.pack(pady=10)

    link8_button = tk.Button(one_direction_window, text="Story Of My Life", command=lambda: open_link("https://drive.google.com/file/d/16CG2WUNDgjkkPbc67dqgvM2Rrc_dJ4wD/view?usp=drive_link"))
    link8_button.pack(pady=10)

    link9_button = tk.Button(one_direction_window, text="What Makes You Beautiful", command=lambda: open_link("https://drive.google.com/file/d/1674AJOA6SN7_n9S1WTKGX1-KxgEFLDIO/view?usp=drive_link"))
    link9_button.pack(pady=10)

    link10_button = tk.Button(one_direction_window, text="You & I", command=lambda: open_link("https://drive.google.com/file/d/162_zFucrfplipQhhOMM7JNa_8mXf9TVl/view?usp=drive_link"))
    link10_button.pack(pady=10)

    tk.Button(one_direction_window, text="Back to Home", command=lambda: return_to_home(one_direction_window)).pack(pady=10)

    one_direction_window.mainloop()

def open_english_page():
    root.withdraw()
    
    english_window = tk.Tk()
    english_window.title("English Music Library")
    
    english_label = tk.Label(english_window, text="Welcome to the English Music Library!")
    english_label.pack(pady=20)
    
    charlie_puth_button = tk.Button(english_window, text="Charlie Puth", command=lambda: open_charlie_puth_page(english_window))
    charlie_puth_button.pack(pady=10)

    dua_lipa_button = tk.Button(english_window, text="Dua Lipa", command=lambda: open_dua_lipa_page(english_window))
    dua_lipa_button.pack(pady=10)
    
    ed_sheeran_button = tk.Button(english_window, text="Ed Sheeran", command=lambda: open_ed_sheeran_page(english_window))
    ed_sheeran_button.pack(pady=10)

    justin_bieber_button = tk.Button(english_window, text="Justin Bieber", command=lambda: open_justin_bieber_page(english_window))
    justin_bieber_button.pack(pady=10)

    one_direction_button = tk.Button(english_window, text="One Direction", command=lambda: open_one_direction_page(english_window))
    one_direction_button.pack(pady=10)

    back_button = tk.Button(english_window, text="Back to Home", command=lambda: return_to_home(english_window))
    back_button.pack(pady=10)
    
    english_window.mainloop()

def add_suggestion(entry, listbox):
    suggestion = entry.get()
    if suggestion:
        listbox.insert(tk.END, suggestion)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a suggestion.")

def delete_suggestion(listbox):
    selected_items = listbox.curselection()
    if selected_items:
        for index in selected_items[::-1]:
            listbox.delete(index)
    else:
        messagebox.showwarning("Selection Error", "Please select a suggestion to delete.")

def open_suggestion_page():
    root.withdraw()

    suggestion_window = tk.Toplevel()
    suggestion_window.title("Suggestion Box")

    entry = tk.Entry(suggestion_window, width=40)
    entry.grid(row=0, column=0, padx=10, pady=10)

    listbox = tk.Listbox(suggestion_window, selectmode=tk.MULTIPLE, width=40, height=10)
    listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    add_button = tk.Button(suggestion_window, text="Add", command=lambda: add_suggestion(entry, listbox))
    add_button.grid(row=0, column=1, padx=10, pady=10)

    delete_button = tk.Button(suggestion_window, text="Delete", command=lambda: delete_suggestion(listbox))
    delete_button.grid(row=2, column=0, columnspan=2, pady=10)

    back_button = tk.Button(suggestion_window, text="Back to Home", command=lambda: return_to_home(suggestion_window))
    back_button.grid(row=3, column=0, columnspan=2, pady=10)

def return_to_home(current_window):
    global root
    current_window.destroy()
    
    if root.winfo_exists():
        root.deiconify()
    else:
        root = tk.Tk()
        root.title("Music Library")
        
        label = tk.Label(root, text="Select your Language")
        label.pack(pady=10)

        search_entry = tk.Entry(root, width=30)
        search_entry.pack(pady=10)

        search_button = tk.Button(root, text="Search", command=search)
        search_button.pack(pady=5)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=30)
        
        button1 = tk.Button(button_frame, text="Hindi", command=open_hindi_page)
        button2 = tk.Button(button_frame, text="Punjabi", command=open_punjabi_page)
        button3 = tk.Button(button_frame, text="Urdu", command=open_urdu_page)
        button4 = tk.Button(button_frame, text="English", command=open_english_page)
        button5 = tk.Button(button_frame, text="Suggestion", command=open_suggestion_page)

        button1.pack(side="left", padx=10)
        button2.pack(side="left", padx=10)
        button3.pack(side="left", padx=10)
        button4.pack(side="left", padx=10)
        button5.pack(side="left", padx=10)
        
        root.mainloop() 


root = tk.Tk()
root.title("Music Library")

label = tk.Label(root, text="Select your Language")
button_frame = tk.Frame(root)

search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=10)

search_button = tk.Button(root, text="Search", command=search)
search_button.pack(pady=5)

button1 = tk.Button(button_frame, text="Hindi", command=open_hindi_page)
button2 = tk.Button(button_frame, text="Punjabi", command=open_punjabi_page)
button3 = tk.Button(button_frame, text="Urdu", command=open_urdu_page)
button4 = tk.Button(button_frame, text="English", command=open_english_page)
button5 = tk.Button(button_frame, text="Suggestion", command=open_suggestion_page)

label.pack(pady=10)
button1.pack(side="left", padx=10)
button2.pack(side="left", padx=10)
button3.pack(side="left", padx=10)
button4.pack(side="left", padx=10)
button5.pack(side="left", padx=10)
button_frame.pack(pady=30)

root.mainloop()
