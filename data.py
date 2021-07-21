import csv
import json

with open('golf-courses-usa.csv') as file:
    img_dict = {
        "AL": "https://www.northwoodgolf.com/images/slideshows/banner_5.jpg",
        "AK": "https://golf-pass.brightspotcdn.com/dims4/default/6930158/2147483647/strip/true/crop/1280x764+0+44/resize/1440x860!/format/jpg/quality/90/?url=https%3A%2F%2Fgolf-pass-brightspot.s3.amazonaws.com%2Fe5%2Fd7%2F57f53222693f028158c34460e10a%2Fp.php",
        "AR": "https://www.golfcoursearchitecture.net/images/Short-terrors-7_950x534.jpg",
        "AZ": "https://www.allentowngolf.org/images/template/showcase3.jpg",
        "CA": "https://www.annbriar.com/wp-content/uploads/sites/5725/2016/03/Hole-12-Green.jpg",
        "CO": "https://igp.brightspotcdn.com/dims4/default/b5d3cc3/2147483647/strip/true/crop/1080x525+0+42/resize/1926x936!/quality/90/?url=http%3A%2F%2Findigogolf-brightspot.s3.amazonaws.com%2Fclubs%2F06%2F20%2F1ed4c8ba41fc8202380ab75aa5a5%2Fgeorge-dunne-0203.jpg",
        "CT": "https://igp.brightspotcdn.com/dims4/default/09fd6d9/2147483647/strip/true/crop/1024x498+0+87/resize/1926x936!/quality/90/?url=http%3A%2F%2Findigogolf-brightspot.s3.amazonaws.com%2Fclubs%2Fb0%2F23%2F28e764b24aefa19658bebc5d3b4f%2Fdubsdread.jpg",
        "DE": "https://golf-pass.brightspotcdn.com/dims4/default/0950808/2147483647/strip/true/crop/6000x3583+0+208/resize/1440x860!/format/jpg/quality/90/?url=https%3A%2F%2Fgolf-pass-brightspot.s3.amazonaws.com%2F33%2Ff0%2Fd8ada9954fe5a64344ff272f4ee2%2Fgoldeneagle-course-1.jpg",
        "FL": "https://www.bethlehemgc.com/images/home-bg.jpg",
        "GA": "https://www.fairview.distinctgolf.com/wp-content/uploads/sites/7790/2019/03/slide1.jpg",
        "HI": "https://tpc.com/wp-content/uploads/2018/09/f_lv.jpg",
        "ID": "https://tpc.com/wp-content/uploads/2018/09/f_sugar.jpg",
        "GA": "https://tpc.com/wp-content/uploads/2018/09/f_hp.jpg",
        "IL": "https://photo-assets.masters.com/images/pics/large/h_18ANGC11-2m0191Hc.jpg",
        "IN": "https://tpc.com/wp-content/uploads/2018/09/f_riversbend.jpg",
        "IA": "https://tpc.com/wp-content/uploads/2018/09/f_stonebrae.jpg",
        "KS": "https://www.masters.com/images/course/720x405/H_hole15.jpg",
        "KY": "https://golfdigest.sports.sndimg.com/content/dam/images/golfdigest/fullset/2018/07/11/5b46195cca4a3c573b0b5959_12A.jpg.rend.hgtvcom.966.644.suffix/1573245782010.jpeg",
        "LA": "https://golfdigest.sports.sndimg.com/content/dam/images/golfdigest/fullset/2015/08/17/55d24d8db91019d74c98f56b_TPC-San-Antonio-Oaks-Course.jpg.rend.hgtvcom.966.544.suffix/1573513774287.jpeg",
        "ME": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.northwoodgolf.com%2Fimages%2Fslideshows%2Fbanner_4.jpg&imgrefurl=https%3A%2F%2Fwww.northwoodgolf.com%2F&tbnid=AovG6iUI-M8YpM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygiegUIARC9Ag..i&docid=pplwPm_JmF0gMM&w=2000&h=1250&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygiegUIARC9Ag",
        "MD": "https://www.dyedesigns.com/wp-content/uploads/2017/05/TPCSawgrass16.jpg",
        "MA": "https://golf-pass.brightspotcdn.com/dims4/default/25b051f/2147483647/strip/true/crop/1000x597+0+34/resize/1440x860!/format/jpg/quality/90/?url=https%3A%2F%2Fgolf-pass-brightspot.s3.amazonaws.com%2Fe5%2F2a%2Ff27f3d9e73d3bd9361046c8299aa%2Fp.php",
        "MI": "https://tpc.com/colorado/wp-content/uploads/sites/59/2019/09/Mobile-Callout-TPC-Colorado-450x240.jpg",
        "MD": "https://golf-pass.brightspotcdn.com/dims4/default/c2741e7/2147483647/strip/true/crop/2736x1538+0+218/resize/900x506!/quality/90/?url=https%3A%2F%2Fgolf-pass-brightspot.s3.amazonaws.com%2F25%2F38%2F3b492cd47e7493fceb233c14f35c%2Fp.php",
        "MN": "https://golf.com/wp-content/uploads/2021/03/tpc-sawgrass-price.jpg",
        "MS": "https://tpc.com/scottsdale/wp-content/uploads/sites/50/2016/08/Scottsdale-hole-5-compressed.jpg",
        "MO": "https://www.pgatour.com/content/dam/pgatour/courses/r011/011/holes/hole4.jpg",
        "MT": "https://lh3.googleusercontent.com/proxy/okho9iFZ2y8KriU76EaHhQs3yHaeGLhXS0RZIdmc3ozgSEZMxZLKPPJXdkRA0fq_KPKMTqFeAsaZnxYBF-jIzomy7hw42_DOsI4vfD-5MCH0w9ZvkPWWdVp_4qpZULsbvpv74E6htWBLpJkid94rkJWfvlc0p_Lbmp7iFawISTj7iBXYbRzw",
        "ND": "https://www.masters.com/images/course/720x405/H_hole17.jpg",
        "NE": "https://www.lodgetorreypines.com/sites/default/files/styles/gallery/public/2019-06/golf11.jpg?itok=_x4KHXEY",
        "NV": "https://www.opkansas.org/wp-content/uploads/2019/06/sykes-lady-trees-web.jpg",
        "NH": "https://www.opkansas.org/wp-content/uploads/2019/06/St-Andrews-32-of-41web.jpg",
        "NJ": "https://www.opkansas.org/wp-content/uploads/2019/06/St-Andrews-32-of-41web.jpg",
        "NM": "https://golf-pass.brightspotcdn.com/dims4/default/e95a0ca/2147483647/strip/true/crop/1080x697+0+12/resize/930x600!/quality/90/?url=https%3A%2F%2Fgolf-pass-brightspot.s3.amazonaws.com%2F99%2F2c%2F4c3bfcea0b05ccdfe1c5fbd7b63e%2F70952.jpg",
        "NC": "https://www.cityofdenvergolf.com/golf/proto/cityofdenvergolf/images/gallery/Overland%20Park/10.jpg",
        "NY": "https://www.masters.com/images/course/720x405/H_hole14.jpg",
        "OH": "https://www.pebblebeach.com/content/uploads/pbgl-7thhole-wave-bartkeagy-1-1067x600.jpg",
        "OK": "https://thegolfnewsnet.com/wp-content/uploads/2016/05/Monterey-Pebble-Beach.jpg",
        "OR": "https://photo-assets.masters.com/images/pics/large/h_01ANGC12-rb4351H.jpg",
        "PA": "https://golfweek.usatoday.com/wp-content/uploads/sites/87/2019/03/pebble-7th.jpg?w=1000&h=600&crop=1",
        "RI": "https://golfdigest.sports.sndimg.com/content/dam/images/golfdigest/fullset/2021/4/pebble%20beach%20aerial%20joann%20dost%20hero.jpg.rend.hgtvcom.966.483.suffix/1619753399071.jpeg",
        "SC": "https://golfdigest.sports.sndimg.com/content/dam/images/golfdigest/fullset/2021/4/pebble%20beach%20aerial%20joann%20dost%20hero.jpg.rend.hgtvcom.966.483.suffix/1619753399071.jpeg",
        "SD": "https://www.amateurgolf.com/images/uploads/00060090.jpg",
        "TN": "https://photo-assets.masters.com/images/pics/large/h_01ANGC08FALL-rb0560c.jpg",
        "TX": "https://www.masters.com/images/course/720x405/H_hole2.jpg",
        "UT": "https://www.masters.com/images/course/720x405/H_hole3.jpg",
        "VT": "https://www.masters.com/images/course/720x405/H_hole5.jpg",
        "VA": "https://www.masters.com/images/course/720x405/H_hole4.jpg",
        "WA": "https://www.masters.com/images/course/720x405/H_hole6.jpg",
        "WV": "https://www.masters.com/images/course/720x405/H_hole9.jpg",
        "WI": "https://www.masters.com/images/course/720x405/H_hole11.jpg",
        "WY": "https://www.masters.com/images/course/720x405/H_hole12.jpg",
        "DC": "https://www.masters.com/images/course/720x405/H_hole13.jpg"
    }
    dict_list = []
    reader = csv.reader(file)
    for row in reader:
        dict = {
            "name": "", 
            "_geoloc": {
                "lng": 0, 
                "lat": 0
                },
            "state": "",
            "type": "",
            "num_holes": 0,
            "address": "",
            "city": "",
            "zip_code": "",
            "phone": "",
            }
        dict["_geoloc"]['lng'] = float(row[0])
        dict["_geoloc"]['lat'] = float(row[1])
        name_state_list = (row[2].split(','))
        try:
            dict["phone"] = row[3].split(', ')[3]
        except IndexError:
            dict["phone"] = '(123) 456-7890'
        dict["name"] = name_state_list[0]
        dict["state"] = row[2][-2:len(row[2])]
        type_holes_address_phone_list = row[3].split(')')
        dict["type"] = type_holes_address_phone_list[0].replace('(', '')
        dict["num_holes"] = type_holes_address_phone_list[1].replace(' (', '')
        new_list = type_holes_address_phone_list[2].split(', ')
        try: 
            city_state_zip = new_list[2].split(',')
            dict["zip_code"] = city_state_zip[1][3:]
        except IndexError:
            continue
        dict["address"] = new_list[1]
        dict["city"] = city_state_zip[0]
        dict["img_url"] = img_dict[dict["state"]]
        print(dict)
        dict_list.append(dict)

with open('index.json', 'w') as json_file:
    json_file.write(json.dumps(dict_list))
