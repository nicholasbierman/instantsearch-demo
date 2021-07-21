import csv
import json

with open('golf-courses-usa.csv') as file:
    img_dict = {
        "AL": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.northwoodgolf.com%2Fimages%2Fslideshows%2Fbanner_5.jpg&imgrefurl=https%3A%2F%2Fwww.northwoodgolf.com%2F&tbnid=MXY9yoD-IzeudM&vet=12ahUKEwi7-oTCz_LxAhWPdqwKHZkAAY0QMygAegUIARDxAQ..i&docid=pplwPm_JmF0gMM&w=2000&h=1250&q=golf%20course%20images&ved=2ahUKEwi7-oTCz_LxAhWPdqwKHZkAAY0QMygAegUIARDxAQ",
        "AK": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.curriegolf.com%2F&psig=AOvVaw0-ZcRohVqrkRoLrea4Q_PX&ust=1626903917665000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCMCEtsTP8vECFQAAAAAdAAAAABA7",
        "AR": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fgolf.com%2Fwp-content%2Fuploads%2F2020%2F11%2FTexarkana.jpg&imgrefurl=https%3A%2F%2Fgolf.com%2Ftravel%2Fbest-golf-courses-arkansas-2020-2021-ranking%2F&tbnid=-zHp1briUkD7RM&vet=12ahUKEwjfzZGy0PLxAhVa66wKHZv_Ae8QMygAegUIARCtAQ..i&docid=wnShPDCYIm5wvM&w=1856&h=1044&q=arkansas%20golf%20course&ved=2ahUKEwjfzZGy0PLxAhVa66wKHZv_Ae8QMygAegUIARCtAQ",
        "AZ": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwekopa.com%2Fwp-content%2Fuploads%2F2015%2F06%2Fslide-saguaro8-1024x638.jpg&imgrefurl=https%3A%2F%2Fwekopa.com%2F&tbnid=suNDq36dBkyImM&vet=12ahUKEwihudm00fLxAhVGZKwKHbokCzUQMygAegUIARCqAQ..i&docid=WAIuo0RzYBlTyM&w=1024&h=638&itg=1&q=We-Ko-Pa%20Golf%20Club&ved=2ahUKEwihudm00fLxAhVGZKwKHbokCzUQMygAegUIARCqAQ",
        "CA": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fthehighlandsgc.com%2Fwp-content%2Fuploads%2F2020%2F03%2Fhighlandshomeheader1-1500x630.jpg&imgrefurl=https%3A%2F%2Fthehighlandsgc.com%2F&tbnid=hBMJHQ3y6cRoOM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygFegUIARD7AQ..i&docid=GYzf33yijOQ3FM&w=1500&h=630&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygFegUIARD7AQ",
        "CO": "https://www.google.com/imgres?imgurl=https%3A%2F%2Figp.brightspotcdn.com%2Fdims4%2Fdefault%2F09fd6d9%2F2147483647%2Fstrip%2Ftrue%2Fcrop%2F1024x498%2B0%2B87%2Fresize%2F1926x936!%2Fquality%2F90%2F%3Furl%3Dhttp%253A%252F%252Findigogolf-brightspot.s3.amazonaws.com%252Fclubs%252Fb0%252F23%252F28e764b24aefa19658bebc5d3b4f%252Fdubsdread.jpg&imgrefurl=https%3A%2F%2Fwww.historicaldubsdread.com%2F&tbnid=2T8iP-qThvaWZM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygGegUIARD9AQ..i&docid=pFXPKlC6ZXBftM&w=1926&h=936&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygGegUIARD9AQ",
        "CT": "https://www.google.com/imgres?imgurl=https%3A%2F%2Figp.brightspotcdn.com%2Fdims4%2Fdefault%2F17ec652%2F2147483647%2Fstrip%2Ftrue%2Fcrop%2F2400x1350%2B0%2B0%2Fresize%2F1024x576!%2Fquality%2F90%2F%3Furl%3Dhttp%253A%252F%252Findigogolf-brightspot.s3.amazonaws.com%252Fclubs%252F80%252Fd3%252F702122c5410eb0db6133dacb3b3f%252Fcrc-avon-fields-golf-course.jpg&imgrefurl=https%3A%2F%2Fwww.cincygolf.org%2F&tbnid=1xcLvLTMEdx4uM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygHegUIARD_AQ..i&docid=vo4xxTDc2qJkNM&w=1024&h=576&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygHegUIARD_AQ",
        "DE": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.pendletongolfva.com%2Fimages%2Fslideshows%2Fpendleton-slide-1.jpg&imgrefurl=https%3A%2F%2Fwww.pendletongolfva.com%2F&tbnid=feVGv78lFd2QoM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygIegUIARCBAg..i&docid=nK0K4ySS9TVG6M&w=1600&h=870&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygIegUIARCBAg",
        "FL": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.annbriar.com%2Fwp-content%2Fuploads%2Fsites%2F5725%2F2016%2F03%2FHole-12-Green.jpg&imgrefurl=https%3A%2F%2Fwww.annbriar.com%2F&tbnid=tDiFBS5KpUm7PM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygJegUIARCDAg..i&docid=eiBoYemRuXFDoM&w=6000&h=4000&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygJegUIARCDAg",
        "GA": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.fairview.distinctgolf.com%2Fwp-content%2Fuploads%2Fsites%2F7790%2F2019%2F03%2Fslide1.jpg&imgrefurl=https%3A%2F%2Fwww.fairview.distinctgolf.com%2F&tbnid=H7cOwLRmn_s76M&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygKegUIARCFAg..i&docid=EgnzxW1FZhnrkM&w=1920&h=735&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygKegUIARCFAg",
        "HI": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fgolf-pass.brightspotcdn.com%2Fdims4%2Fdefault%2F0950808%2F2147483647%2Fstrip%2Ftrue%2Fcrop%2F6000x3583%2B0%2B208%2Fresize%2F1440x860!%2Fformat%2Fjpg%2Fquality%2F90%2F%3Furl%3Dhttps%253A%252F%252Fgolf-pass-brightspot.s3.amazonaws.com%252F33%252Ff0%252Fd8ada9954fe5a64344ff272f4ee2%252Fgoldeneagle-course-1.jpg&imgrefurl=https%3A%2F%2Fwww.golfpass.com%2Ftravel-advisor%2Farticles%2Fhow-to-golf-course-comeback&tbnid=17c1oXoydsXv4M&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygLegUIARCHAg..i&docid=MymUXx5c51VffM&w=1440&h=860&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygLegUIARCHAg",
        "ID": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.ctfassets.net%2F56u5qdsjym8c%2F3b96eGN9KodYhSYaBsYpI%2F261024d195ef6803bca98d4e10fd2793%2FBlue-Doral-Monster-Hero.jpg%3Ffl%3Dprogressive%26q%3D80&imgrefurl=https%3A%2F%2Fwww.pga.com%2Fstory%2Fbest-courses-in-south-florida&tbnid=5_Hrs6rB2Ep_yM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygSegUIARCVAg..i&docid=dx35gILJD4YC0M&w=1800&h=1200&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygSegUIARCVAg",
        "GA": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fgolfscape.com%2Fblog%2Fwp-content%2Fuploads%2F2018%2F11%2Faphrodite-hills-golf-course.jpg&imgrefurl=https%3A%2F%2Fgolfscape.com%2Fblog%2F20-worlds-best-golf-courses-to-play-before-you-die%2F&tbnid=O5pqzErxD1gV_M&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygUegUIARCZAg..i&docid=byqRXEZnrn4XbM&w=1600&h=900&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygUegUIARCZAg",
        "ID": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fa%2Fae%2FGreat_Waters_at_Reynolds_Lake_Oconee_-_Oct_2019.jpg&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FList_of_golf_courses_designed_by_Jack_Nicklaus&tbnid=CL6ZRH4HUKq-VM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygZegUIARCqAg..i&docid=dc0xfHOGrpmYrM&w=1800&h=886&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygZegUIARCqAg",
        "IL": "https://www.google.com/imgres?imgurl=https%3A%2F%2Figp.brightspotcdn.com%2Fdims4%2Fdefault%2F73df936%2F2147483647%2Fstrip%2Ftrue%2Fcrop%2F2400x1166%2B0%2B92%2Fresize%2F1926x936!%2Fquality%2F90%2F%3Furl%3Dhttp%253A%252F%252Findigogolf-brightspot.s3.amazonaws.com%252Fclubs%252Fa8%252F40%252F9700ad9248d6b48f433f0327dcc8%252Falhambra-golf-course-14.jpg&imgrefurl=https%3A%2F%2Fwww.alhambragolf.com%2F&tbnid=RTloqm0UsyfyoM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygaegUIARCsAg..i&docid=g3hTssiThrmf4M&w=1926&h=936&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygaegUIARCsAg",
        "IN": "https://www.google.com/imgres?imgurl=https%3A%2F%2Figp.brightspotcdn.com%2Fdims4%2Fdefault%2Fc4fb478%2F2147483647%2Fstrip%2Ftrue%2Fcrop%2F1920x1008%2B0%2B36%2Fresize%2F1200x630!%2Fquality%2F90%2F%3Furl%3Dhttp%253A%252F%252Findigogolf-brightspot.s3.amazonaws.com%252Fclubs%252F87%252Fda%252F3d2d388e4d42bd18b197d1ebad92%252Findian-boundary-0032.jpg&imgrefurl=https%3A%2F%2Findianboundary.forestpreservegolf.com%2F&tbnid=JwU2hdCHzcoNzM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygcegUIARCwAg..i&docid=klwLm2VbpI9ZEM&w=1200&h=630&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygcegUIARCwAg",
        "IA": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.pennstategolfcourses.com%2Fimages%2Fslideshows%2Fbanner_1.jpg&imgrefurl=https%3A%2F%2Fwww.pennstategolfcourses.com%2F&tbnid=JIq8OA0QxAdQpM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygdegUIARCyAg..i&docid=E2wuNPcivrV1zM&w=1200&h=652&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygdegUIARCyAg",
        "KS": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fphotos%2Fgolf-green-and-tee-box-in-late-afternoon-sunlight-picture-id176834848%3Fk%3D6%26m%3D176834848%26s%3D612x612%26w%3D0%26h%3D_4c50EahAyuHOt_CuS3yxZVs7zZXC4ew2FCS03pYXTo%3D&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fgolf-course&tbnid=TVzJclghah-3EM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygeegUIARC0Ag..i&docid=fDAPqoPtGP3piM&w=612&h=408&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygeegUIARC0Ag",
        "KY": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.cybergolf.com%2Fimages%2F2279%2FBellevue_36-H10_1920x1280.jpg&imgrefurl=http%3A%2F%2Fwww.bellevuepgc.com%2F&tbnid=i3EyrKk9F5wGfM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMyggegUIARC5Ag..i&docid=KSc8rIoQRlHYyM&w=1920&h=1280&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMyggegUIARC5Ag",
        "LA": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.villagelinksgolf.com%2Fimages%2Fslideshows%2Fbanner_1.jpg&imgrefurl=https%3A%2F%2Fwww.villagelinksgolf.com%2F&tbnid=7yDMYaQ6NKuy0M&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMyghegUIARC7Ag..i&docid=1QSRIvLdC5S8bM&w=1900&h=1032&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMyghegUIARC7Ag",
        "ME": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.northwoodgolf.com%2Fimages%2Fslideshows%2Fbanner_4.jpg&imgrefurl=https%3A%2F%2Fwww.northwoodgolf.com%2F&tbnid=AovG6iUI-M8YpM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygiegUIARC9Ag..i&docid=pplwPm_JmF0gMM&w=2000&h=1250&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygiegUIARC9Ag",
        "MD": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.cybergolf.com%2Fimages%2F2282%2FLegion-Memorial-New-Hole_1920x1280_r2.jpg&imgrefurl=http%3A%2F%2Feverettgolf.com%2F&tbnid=FSz_9mW8mWYXAM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygjegUIARC_Ag..i&docid=oVtcYOl7zUbYBM&w=1920&h=1280&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygjegUIARC_Ag",
        "MA": "https://www.google.com/imgres?imgurl=https%3A%2F%2Figp.brightspotcdn.com%2Fdims4%2Fdefault%2Ff9f2676%2F2147483647%2Fstrip%2Ftrue%2Fcrop%2F2200x1237%2B0%2B0%2Fresize%2F840x472!%2Fquality%2F90%2F%3Furl%3Dhttp%253A%252F%252Findigogolf-brightspot.s3.amazonaws.com%252Fclubs%252F6b%252F90%252Fac06e8b648cbb74836c1fc645f7b%252Fthe-ridge-golf-course-16.9-1.jpg&imgrefurl=https%3A%2F%2Fwww.ridgegc.com%2F&tbnid=x357rzNQKamnKM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygkegUIARDBAg..i&docid=Z0IlFkqBX7xWaM&w=840&h=472&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygkegUIARDBAg",
        "MI": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.lakewood.org%2Ffiles%2Fassets%2Fpublic%2Fcommunity-resources%2Fgolf%2Fhomesteadgcclubdji-0700.jpg%3Fdimension%3Dpageimagefullwidth%26w%3D1140%26h%3D540&imgrefurl=https%3A%2F%2Fwww.lakewood.org%2FGovernment%2FDepartments%2FCommunity-Resources%2FLakewood-Golf%2FHomestead-Golf-Course&tbnid=b3b4O4F1rmS5XM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygpegUIARDLAg..i&docid=NWtxIxf6kK7CHM&w=1140&h=540&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygpegUIARDLAg",
        "MD": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.timberlinegc.com%2Fimages%2Fslideshows%2Fbanner_1.jpg&imgrefurl=https%3A%2F%2Fwww.timberlinegc.com%2F&tbnid=PhRL7-B9ZvfycM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygxegQIARB8..i&docid=2opkvgHR0ZVvcM&w=1280&h=400&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMygxegQIARB8",
        "MN": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.pipestonegolf.com%2Fimages%2Fslideshows%2Fbanner_1.jpg&imgrefurl=https%3A%2F%2Fwww.pipestonegolf.com%2F&tbnid=JIPVjWLOGfCLMM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMyhYegUIARDRAQ..i&docid=xxcCsgAnOdv9WM&w=1920&h=1112&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMyhYegUIARDRAQ",
        "MS": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.golfbuffalohill.com%2Fwp-content%2Fuploads%2Fsites%2F8067%2F2021%2F02%2F12-Homepage-2.jpg&imgrefurl=https%3A%2F%2Fwww.golfbuffalohill.com%2F&tbnid=a514WM4rLUbxqM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMyhcegUIARDZAQ..i&docid=hnDkdKYum0leYM&w=5760&h=1891&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMyhcegUIARDZAQ",
        "MO": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fbellavistapoa.com%2Fwp-content%2Fuploads%2F2020%2F05%2Fgolf.jpg&imgrefurl=https%3A%2F%2Fbellavistapoa.com%2Fthingstodo%2Fgolf%2F&tbnid=oBcmueLHqOnNgM&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMyhhegUIARDqAQ..i&docid=M445_DqFKr4bSM&w=1500&h=430&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMyhhegUIARDqAQ",
        "MT": "https://www.google.com/imgres?imgurl=https%3A%2F%2Figp.brightspotcdn.com%2Fdims4%2Fdefault%2F5dabafb%2F2147483647%2Fstrip%2Ftrue%2Fcrop%2F2135x1038%2B0%2B81%2Fresize%2F1926x936!%2Fquality%2F90%2F%3Furl%3Dhttp%253A%252F%252Findigogolf-brightspot.s3.amazonaws.com%252Fclubs%252Fc0%252F4b%252F62fbb2a64214b53fc69ad4bfed5c%252Ftri-mountain-golf-course-5.jpg&imgrefurl=https%3A%2F%2Fwww.trimountaingolf.com%2F&tbnid=kBrhdyjZmFPA5M&vet=12ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMyhiegUIARDsAQ..i&docid=QLmjv4-YbQQAmM&w=1926&h=936&q=golf%20course%20images&ved=2ahUKEwiXpo_T0vLxAhULa60KHa-mAfgQMyhiegUIARDsAQ",
        "NE": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.cybergolf.com%2Fimages%2F2288%2Fslide1_1920x480.jpg&imgrefurl=https%3A%2F%2Fwww.allingmemorialgolfclub.com%2F&tbnid=Ax1871deid6gcM&vet=10CAEQMyhkahcKEwig-uPT0vLxAhUAAAAAHQAAAAAQBA..i&docid=XxCCnfniwWbkCM&w=1920&h=480&q=golf%20course%20images&ved=0CAEQMyhkahcKEwig-uPT0vLxAhUAAAAAHQAAAAAQBA",
        "NV": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.stonecreekgolfocala.com%2Fimages%2Fslideshows%2Fbanner_1.jpg&imgrefurl=https%3A%2F%2Fwww.stonecreekgolfocala.com%2F&tbnid=N9dY6E11bQ1ORM&vet=10CAsQMyhpahcKEwig-uPT0vLxAhUAAAAAHQAAAAAQBA..i&docid=neDS_hGkAZteIM&w=1920&h=1112&q=golf%20course%20images&ved=0CAsQMyhpahcKEwig-uPT0vLxAhUAAAAAHQAAAAAQBA",
        "NH": "https://www.google.com/imgres?imgurl=https%3A%2F%2Findiancreekgolf.com%2Fwp-content%2Fuploads%2F2019%2F04%2FDJI_0186-1267x630.jpg&imgrefurl=https%3A%2F%2Findiancreekgolf.com%2F&tbnid=YuZXCmN8TKsbOM&vet=10CA0QMyhqahcKEwig-uPT0vLxAhUAAAAAHQAAAAAQBA..i&docid=XNI0-MajtRcanM&w=1267&h=630&q=golf%20course%20images&ved=0CA0QMyhqahcKEwig-uPT0vLxAhUAAAAAHQAAAAAQBA",
        "NJ": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.westfieldsgolf.com%2F&psig=AOvVaw3CMm8Tx2Tud26VPpBNwEIC&ust=1626904758793000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCKD649PS8vECFQAAAAAdAAAAABAG",
        "NM": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.woodstockinn.com%2Fdo%2Fthings-to-do%2Fgolf%2Fthe-course&psig=AOvVaw3CMm8Tx2Tud26VPpBNwEIC&ust=1626904758793000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCKD649PS8vECFQAAAAAdAAAAABAM",
        "NY": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.quinterogolf.com%2Fwp-content%2Fuploads%2F2020%2F03%2Fbkg-hole-1.jpg&imgrefurl=https%3A%2F%2Fwww.quinterogolf.com%2Fchampionship-golf-course-phoenix%2F&tbnid=ys3TufLRAUbr4M&vet=10CDoQMyh9ahcKEwig-uPT0vLxAhUAAAAAHQAAAAAQBA..i&docid=7tRMr6Us5iXgcM&w=1800&h=878&q=golf%20course%20images&ved=0CDoQMyh9ahcKEwig-uPT0vLxAhUAAAAAHQAAAAAQBA",
        "NC": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.willowsrun.com%2FPortals%2F33%2FWebSitesCreative_SliderRevolutionImporter%2FImages%2F5379%2F5e32b-DJI_0113-New.jpg&imgrefurl=https%3A%2F%2Fwww.willowsrun.com%2F&tbnid=i9Mm7dkKo6nWnM&vet=10CEYQMyiDAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEAQ..i&docid=tUGJwARqwOX5DM&w=2000&h=1332&q=golf%20course%20images&ved=0CEYQMyiDAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEAQ",
        "ND": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fgolfdigest.sports.sndimg.com%2Fcontent%2Fdam%2Fimages%2Fgolfdigest%2Ffullset%2F2015%2F08%2F04%2F55c1221e4759c60c08234b38_pine-valley-gc-18.jpg.rend.hgtvcom.1280.853.suffix%2F1573512242882.jpeg&imgrefurl=https%3A%2F%2Fwww.golfdigest.com%2Fstory%2Fworlds-100-greatest-golf-courses-2016-ranking&tbnid=ztLW1tCguqxzCM&vet=10CGkQMyiRAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEAQ..i&docid=jJfTh28_YdlQ9M&w=1280&h=853&q=golf%20course%20images&ved=0CGkQMyiRAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEAQ",
        "OH": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fgolfweek.usatoday.com%2Fwp-content%2Fuploads%2Fsites%2F87%2F2018%2F09%2Fyale.jpg%3Fw%3D1000%26h%3D600%26crop%3D1&imgrefurl=https%3A%2F%2Fgolfweek.usatoday.com%2F2020%2F09%2F30%2Fyale-golf-course-reopens-free-golf-students%2F&tbnid=cFE50KcmMXXe0M&vet=10CG0QMyiTAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEAQ..i&docid=iRNW-IBJlmDIwM&w=1000&h=600&q=golf%20course%20images&ved=0CG0QMyiTAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEAQ",
        "OK": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fgolfcourse.uga.edu%2F_resources%2Fimages%2FHole-13_900x600.jpg&imgrefurl=https%3A%2F%2Fgolfcourse.uga.edu%2F&tbnid=T4kRbSmL-7aN2M&vet=10CH8QMyicAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEAQ..i&docid=atR_JQq7ATYffM&w=900&h=600&q=golf%20course%20images&ved=0CH8QMyicAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEAQ",
        "OR": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwaileagolf.com%2FPortals%2F35%2FWebSitesCreative_SliderRevolutionImporter%2FImages%2F4957%2F336c5-Wailea-Emerald--10_17_Brian-Oar_8x5.jpg&imgrefurl=https%3A%2F%2Fwaileagolf.com%2F&tbnid=Qg2RmMVeAUMWiM&vet=10CI0BEDMoowFqFwoTCKD649PS8vECFQAAAAAdAAAAABAE..i&docid=dwmMWGbcdbTpOM&w=2000&h=1139&q=golf%20course%20images&ved=0CI0BEDMoowFqFwoTCKD649PS8vECFQAAAAAdAAAAABAE",
        "PA": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.brooklinegolf.com%2Fimages%2FHole-17-banner-2.jpg&imgrefurl=https%3A%2F%2Fwww.brooklinegolf.com%2F&tbnid=_MGzqicOM0daIM&vet=10CK0BEDMorwFqFwoTCKD649PS8vECFQAAAAAdAAAAABAE..i&docid=kUNg_UiClcgt9M&w=1658&h=977&q=golf%20course%20images&ved=0CK0BEDMorwFqFwoTCKD649PS8vECFQAAAAAdAAAAABAE",
        "RI": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.golfdigest.com%2Fcontent%2Fdam%2Fimages%2Fgolfdigest%2Ffullset%2F2015%2F08%2F18%2F55d37f384759c60c08237c53_Belgrade-Lake-Golf-Club.jpg&imgrefurl=https%3A%2F%2Fwww.golfdigest.com%2Fstory%2Fmaine-best-in-state-rankings&tbnid=jFzmSUX_mBC2-M&vet=10CMkBEDMovQFqFwoTCKD649PS8vECFQAAAAAdAAAAABAE..i&docid=b4sK8i3gR7wOJM&w=1927&h=1119&q=golf%20course%20images&ved=0CMkBEDMovQFqFwoTCKD649PS8vECFQAAAAAdAAAAABAE",
        "SC": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.squarespace-cdn.com%2Fcontent%2Fv1%2F54f8cef9e4b0e1531ace9ea8%2F1609529547977-E0JA9AD4DGV1JWZQQCJ6%2FLynxGC920_D0081.jpg%3Fformat%3D2500w&imgrefurl=https%3A%2F%2Flynxgc.com%2F&tbnid=6WsN0ILsTSkqfM&vet=10COIBEDMoxgFqFwoTCKD649PS8vECFQAAAAAdAAAAABAE..i&docid=4PQr02cEvXEQUM&w=2500&h=1524&q=golf%20course%20images&ved=0COIBEDMoxgFqFwoTCKD649PS8vECFQAAAAAdAAAAABAE",
        "SD": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fd1pdyfnmzhu191.cloudfront.net%2Fimages%2Flibrariesprovider2%2Fgolf%2Fbmgc_course_800x533.jpg&imgrefurl=https%3A%2F%2Fwww.bigbearmountainresort.com%2Fthings-to-do%2Fgolf-course&tbnid=8hFWyzOgYH_2BM&vet=10COQBEDMoxwFqFwoTCKD649PS8vECFQAAAAAdAAAAABAE..i&docid=tqtO7B_3CILuMM&w=800&h=533&q=golf%20course%20images&ved=0COQBEDMoxwFqFwoTCKD649PS8vECFQAAAAAdAAAAABAE",
        "TN": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.clevelandmetroparks.com%2Fgetmedia%2F0c62b197-f717-4a7e-bcb1-051b9fc83c26%2FManakiki_Carousel_02.jpg.ashx%3Fh%3D200%26w%3D200%26mode%3Dcrop%26scale%3Dboth&imgrefurl=https%3A%2F%2Fwww.clevelandmetroparks.com%2Fgolf%2Fcourses%2Fmanakiki-golf-course&tbnid=fXngmJu8UeJWvM&vet=10CAEQMyjIAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEBE..i&docid=LvKmSgeLiGAGUM&w=1920&h=1152&q=golf%20course%20images&ved=0CAEQMyjIAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEBE",
        "TX": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.cityofdenvergolf.com%2Fgolf%2Femailer2020%2Fimg%2Fcityofdenvergolf%2FOverland_Hole_1a_NEW(1).jpg&imgrefurl=https%3A%2F%2Fwww.cityofdenvergolf.com%2Foverland_park&tbnid=6FJlu0su4sQlAM&vet=10CBkQMyjUAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEBE..i&docid=Yy7ZOMrjt3vGjM&w=540&h=360&q=golf%20course%20images&ved=0CBkQMyjUAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEBE",
        "UT": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.cityofdenvergolf.com%2Fgolf%2Femailer2020%2Fimg%2Fcityofdenvergolf%2FOverland_Hole_1a_NEW(1).jpg&imgrefurl=https%3A%2F%2Fwww.cityofdenvergolf.com%2Foverland_park&tbnid=6FJlu0su4sQlAM&vet=10CBkQMyjUAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEBE..i&docid=Yy7ZOMrjt3vGjM&w=540&h=360&q=golf%20course%20images&ved=0CBkQMyjUAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEBE",
        "VT": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fassets.simpleviewinc.com%2Fsimpleview%2Fimage%2Fupload%2Fc_limit%2Ch_1200%2Cq_75%2Cw_1200%2Fv1%2Fclients%2Fvirginia%2FHR20020701P_100_1__2ef6fbbb-074b-4070-abf5-d96e22121bf7.jpg&imgrefurl=https%3A%2F%2Fwww.virginia.org%2Fgolf%2F&tbnid=zcuvzBo_4a-YlM&vet=10CDIQMyjcAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEBE..i&docid=R8NSqmGQZV4QpM&w=1200&h=898&q=golf%20course%20images&ved=0CDIQMyjcAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEBE",
        "VA": "https://www.google.com/imgres?imgurl=https%3A%2F%2Figp.brightspotcdn.com%2Fdims4%2Fdefault%2Fc8e3fa3%2F2147483647%2Fstrip%2Ftrue%2Fcrop%2F1920x933%2B0%2B73%2Fresize%2F1926x936!%2Fquality%2F90%2F%3Furl%3Dhttp%253A%252F%252Findigogolf-brightspot.s3.amazonaws.com%252Fclubs%252F92%252F12%252F6f76722f43ecbac2c7a6ef722e7a%252Fwhisper-creek-hole-18-0106.jpg&imgrefurl=https%3A%2F%2Fwww.whispercreekgolf.com%2F&tbnid=ORcP6THGMsc0_M&vet=10CFYQMyjtAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEBE..i&docid=DzA7dFmjSBgk_M&w=1926&h=936&q=golf%20course%20images&ved=0CFYQMyjtAWoXChMIoPrj09Ly8QIVAAAAAB0AAAAAEBE",
        "WA": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fphoto-assets.masters.com%2Fimages%2Fpics%2Flarge%2Fh_12ANGC12-2rb3140Hc.wb.jpg&imgrefurl=https%3A%2F%2Fwww.masters.com%2Fen_US%2Fcourse%2Fhole12.html&tbnid=aVKq42t9PyWW6M&vet=12ahUKEwiEw-_d1PLxAhUN9awKHWqDC_wQMygBegUIARDnAQ..i&docid=1ClGgMbRYiI3WM&w=1440&h=810&q=12%20at%20augusta&ved=2ahUKEwiEw-_d1PLxAhUN9awKHWqDC_wQMygBegUIARDnAQ",
        "WV": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fgolf.com%2Fnews%2F8-reasons-why-whistling-straits-will-be-a-phenomenal-ryder-cup-host%2F&psig=AOvVaw2lGyDT_AdAkA4n0wYEgrRS&ust=1626905339867000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPivuunU8vECFQAAAAAdAAAAABAD",
        "WI": "https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww.torreypinesgolfcourse.com%2Fassets%2Fimages%2Ftorrey-pines-north-15-sunset-location-2-72ppi-2000x1353.jpeg&imgrefurl=http%3A%2F%2Fwww.torreypinesgolfcourse.com%2F&tbnid=HNido3hFiM1w8M&vet=12ahUKEwjn3pTv1PLxAhWyoK0KHR-CAYAQMygAegUIARDLAQ..i&docid=LCJzoXa00hH6JM&w=2000&h=1125&q=torrey%20pines&ved=2ahUKEwjn3pTv1PLxAhWyoK0KHR-CAYAQMygAegUIARDLAQ",
        "WY": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fgolf.com%2Fwp-content%2Fuploads%2F2021%2F03%2Ftpc-sawgrass-price.jpg&imgrefurl=https%3A%2F%2Fgolf.com%2Ftravel%2Ftpc-sawgrass-rates-price-players-championship-course%2F&tbnid=3ILkw9D3rpxHKM&vet=12ahUKEwjnrJj11PLxAhVBWqwKHakFBgcQMygAegUIARDKAQ..i&docid=OjVHRONKrdUy7M&w=1856&h=1044&q=tpc%20sawgrass&ved=2ahUKEwjnrJj11PLxAhVBWqwKHakFBgcQMygAegUIARDKAQ",
        "DC": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fgolf-pass.brightspotcdn.com%2Ff4%2Fda%2F8553966264cdde926293691556d4%2F57785.jpg&imgrefurl=https%3A%2F%2Fwww.golfpass.com%2Ftravel-advisor%2Fcourses%2F13014-robert-trent-jones-golf-club&tbnid=T-0UC_ZpCiamqM&vet=12ahUKEwjQ7cby1vLxAhUDTK0KHRT_As0QMygAegUIARCqAQ..i&docid=37UuW0Ix4PRSKM&w=1440&h=720&q=rtj%20golf%20course%20va&ved=2ahUKEwjQ7cby1vLxAhUDTK0KHRT_As0QMygAegUIARCqAQ"
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
