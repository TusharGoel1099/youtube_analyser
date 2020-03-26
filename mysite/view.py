from django.http import HttpResponse
from django.shortcuts import render
from .models import name
def login(request):
    return render(request,"index.html")
def mail(request):
    name_=request.POST.get("name","not avaiable")
    email_=request.POST.get("email","not available")
    message_=request.POST.get("message","not available")
    import smtplib
    gmailaddress = "frappers100@gmail.com"
    gmailpassword = "******"
    mailto ='tushargoel1099@gmail.com'
    msg = f"{name_} with {email_} sharing this [[ {message_} ]] with you"
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.starttls()
    mailServer.login(gmailaddress, gmailpassword)
    mailServer.sendmail(gmailaddress, mailto, msg)
    print(" \n Sent!")
    mailServer.quit()
    return render(request,"index.html")
       
def hey(request):
    kl=request.POST.get('fname',"not available")
    y=request.POST.get("lname","not available")
    z=request.POST.get("search","not available")
    
    from bs4 import BeautifulSoup as bs4
    import requests
    import pandas as pd
    from textblob import TextBlob
    polarity=[]
    title=[]
    next_link=[]
    views=[]
    channel=[]
    img_url=[]
    comment_text=[]
    x=z
    x=x.replace(" ","+")
    for i in range(0,2):
        url=(f"https://www.youtube.com/results?search_query={x}&page={i}")
        page=requests.get(url)
        soup=bs4(page.text,"html.parser")
        count=0
        divs2=soup.find_all("div",attrs={"class":"yt-thumb video-thumb"})
        for i in divs2:
            b_img_url=i.find("img",{"data-thumb":True})
            if(b_img_url==None):
                img_url.append("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxEHBhAIBxMREBAREQ8QDxAODRAVDQ8SFBEYFhcSExUkIDQhGBolGxUTITEhJTUtMC46Fx8/ODM4NygtLisBCgoKDQ0OGhAQFysmHSYuKzMrLzUxKy0tLS0tLS8tLS0rKy4tLS0tLS0tKzUtLS0rKy4rLS0tLS0tLTctLS8tLf/AABEIAKgBLAMBEQACEQEDEQH/xAAcAAEAAgIDAQAAAAAAAAAAAAAAAQcCBgMEBQj/xABFEAEAAQQAAgQJBQsNAAAAAAAAEQECAwQFBgcSITEiQVFhcZGUsdEUcoGishMjM0JSU2JjksHSFSQlMjQ1Q0RUc4Khwv/EABsBAQACAwEBAAAAAAAAAAAAAAABBAIFBgMH/8QANREBAAECAgUJCAEFAAAAAAAAAAECEQMEBRMxUZESFCEiMkFSU8EGQ2FxgaGx4dEVI0KC8f/aAAwDAQACEQMRAD8A8VpH0sAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIkCQJAkCQJAkCQJAkCQJAkCQJAkCQJAkCQJAkCQJAkCQJAkCQJAkCQJAkCQJAkCQQkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAACAAAAJAkEggAEgAAAAAAAAAAAAAAxGIAAAAAAAAAAADf+W+j6mfBbtccrdb1qUrTBjrF1KV/OXeKvmp3eVdw8reL1udzum5pqmjAj6z6R6y2jFyXw/FSKYKV+fky3V/7ue8ZfDjuaurSucq959oj0c9vK2hb3auD6cdK+9Opw/DDynSObn3tXFy28u6Vvdq6/s+P4J1VHhhjOezU+9q4yzpwLUp3a2v7Ni+CdVR4Y4I55mfMq4yn+RdT/T6/s+L4Gro8McEc6x/Mq4yV4JqV79fX9nxfA1dHhg53mPMq4ywrwDTu79bX9nx/A1VHhhPPcz5lXGWF3LWjd36uv9GGyn7kanD8MMv6hm/Nq4y4r+UtC/v1sVPm0up7qo1GH4WcaTzke8l5+7yBo7Flfk9t+G7xXY8t9aU/43VrRhVlsOdixhaazdE9aYmPjEellccxcCy8A3fk+zF1t1K3Y8lv9XJbTv7PFWnZNPPRRxMKcObS6bJ53DzVHKp6J743PKea2AAAAAAAAAAAAxkCQJAkCQJAkCQJAkCQJB7vJGhTiXM+DFkpStlla5r6V8dMdJp9bqPbAp5VcNfpTHnCytUxtnoj6/q66m0cQAAAAAAAAAA1npE0KbvLOTLSnh4K25ra+SlKxf8AVrd6qPDM08rDn4NnofGnDzUR3VdE+n3U9LWO0JAkCQJAkCQJAkCQJAkCQQAAAAAAAAAAADduijF1uOZsv5OvH7WS3+FbykdaWi0/VbBpjfP4j9rSX3KgAAOntcVwam7j09rJbjyZaVritvrHXisVpSvdPbTs72M1RE2l604OJVRNdNN4jb8HcZPIAAAAB0eO4vu/BNnD+VgzU9eOrGuL0zD2y1XJxqKt0x+VCUrNJad9BSAAAAAAAAAAACJTYJLBJYJLBJYJLBJYJLBJYJLBJYJLDfeiPt3ty7yY8FPXdk+C5lNsue9oOxh/Or0WWuuZAAAVl0uUniGrS781m+3apZvbDpvZ/sYnzj1eFwLnHb4JGPHd93w0/wAHPdWsU/V5O+30dtPMww8xVTt6VvN6IwcbrU9Wfh/Cx+Xec9TjtaYcd1cOfx4M8W31r+hXuv8Ao9S5Ri01bHM5nI42BPWjo3tjeioAAA4tmnW1r7a+Oy6nrtqidjKntQ+esNfvVvop7mnfRp2spLIJLBJYJLBJYJLBJYJLBJYJLBJYJLDFKAAAAAAAAAAAG/8ARF/a9z5mt9rKt5TbV9HPe0HZw/8Ab0WUuuaAAAVl0uV/pHU/2s327FLN7YdN7P8AYxPnHq0NUdAU1/lV9uGy2t91a+DbZbWt9a/o0p2ymL36GGJFHJma5tG/ctnkPQ4npYY43lpdhj73iy06+1b5JyT4NPNXrfQ2OFFdus43P1ZWa/7PHZHD/jcHs1wADDL+Cu+bX3CadsPnfD+Ct9FPc00Po07WSUAAAAAAAAAAAIAAAAAAAAAAABvvRHd/Pty3y49evquyfFbym2XP+0HYw/nV6LLldcySBIEgrPpb/vLTp+rzUp6a32dilmtsOm0B2MT5x6uhy/yHscTjNvzrYq9vhU+/3U/Rs/F9N3qYYeXqq29ELOb0zg4XVw+tV9uPf9OKyOCcA1uCYuroWUpdWkXZLvCzX+m7yeanYu0YdNGyHNZnOY2Ym+JV9O7g9OWaqSBIEg49i7q6991fFbdX1W1JZU9qHzxh/A2/Np7mnfRZ2sxAAAAAAAAAAADGU2CSwSWCSwSWCSwSWCSwSWCSwSWCSw3bony9XjufF+Vrz+zkt/iWsr2paLT1N8Gmd0/mP0tRdcsAAA4L9PHk2rdrJZbdkspW2y+62lbrKVr29XyI5MXuzjErimaInonbG9zpYAAAAAOjx3N8n4Js5q/i4M13qx1Y1zamXtl6eVjUU75j8qCt7LaUaqz6AmSwSWCSwSWCSwSWCSwSWCSwSWCSwSWEJAAAAAAAAAAAHuckcQpw3mjBmyViy+t2G+te6lMlIp9fqPXBq5NcNfpTBnFy1URtjp4fq67mxcSAAAAAAAAAA1bpI4hTS5XyYp8PPW3DbTx1pWs3/Vpd66PHHqtQ2eiMHWZqme6np/j7qea92YAAAAAAAAAAACJAkCQJAkCQJAkCQJAkCQRXtEN/5b6Ra6uvbq8csvyUtpSlufFFb4p+ctrXtr56d/k8a3h5juqc9nNCzNU14M/SfRtOvz1w7NSfu/V82TDmt/8AMPbXUb2qr0Xm6f8AD7x/Ls283cPu7tvB9OWlPey1tG95zkM1Hu54M6c0aFe7b1vaMfxNZRvYzkszHu6uEuSnMWld3bWt7Ti+JrKd6OaZjy6uEs6cd1K/5nW9pxfFPLp3wx5tj+CeEorx7Tp37Ot7Ti+Jy6d8J5tj+CrhLC7mPSt79rW9pxfFGso3p5pmPLq4S47ua9C3v29b6M9lf3mto3wy5jmfLq4S4r+cuH2d+1ir83r3e6iNbRvZRo7Nz7uXn73SJo69lfk92TPd4rceG+2lfTddSlI9bGcxRCxh6HzVc9MWj5x6XVtzFx7NzBvfKduLbbaVpixW18DHbWvl8da+OvmU8TEmuby6bJZLDytHJp29873ly81wkCQJAkCQJAkCQJAkCQJBEiLkhckLkhckLkhckLkhckLkhckLkhckLkhckQgBIdiAigHYB2AJBAmRNyQuSFyQuSFyQuSFyQuSFyQuSFyQuSFyQuSF2IgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABCQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEgSBIEgSBIEgSBIEgSBIEgSBIEgSBIEgSBIEgSBIEgSBIEgSBIEgSBIEgSBIEgSDEQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/9k=")    
            else:
                img_url.append(b_img_url['data-thumb'])
        divs=soup.find_all("div", attrs={ "class" : "yt-lockup-content"})
        for i in divs:
            z_channel=i.find("a",attrs={"class":"yt-uix-sessionlink spf-link "})
            x_title=i.find("a",attrs={"class":"yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "})
            y_views=i.find("ul",attrs={"class":"yt-lockup-meta-info"})
            if(x_title==None):
                title.append("Not available")
                next_link.append("***")
                count+=1
            else:
                
                next_link.append(x_title["href"].replace("/watch?v=",""))
                title.append(x_title.getText())
            if(y_views==None):
                views.append("Not available")
            else:
                views.append(y_views.getText())
            if(z_channel==None):
                channel.append("Not available")
            else:
                channel.append(z_channel.getText())      
    for i in next_link:
    
        if(i=="***"):
            pass
        else:
            x=requests.get(f"https://www.googleapis.com/youtube/v3/commentThreads?key=enteryourapikey&textFormat=plainText&part=snippet&videoId={i}&maxResults=100")
            dic=x.json()
            try:
                length=len(dic["items"])
                for i in range(0,length):
                    text=dic["items"][i]["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                    comment_text.append(text)
            except:
                print(i)
                comment_text.append("error occur")
            finally:
                comment_text.append("stop")

    negative=0
    positive=0
    neutral=0
    j=0        
    for i in comment_text:
        if(i=="stop"):
            polarity.append({"positive":positive,"negative":negative,"neutral":neutral})
            negative=0
            positive=0
            neutral=0
            j+=1
        result=TextBlob(i).sentiment.polarity
        
        if(result<0):
            result="negative"
            negative+=1
        elif(result==0):
            result="neutral"
            neutral+=1
        else:
            result="positive"
            positive+=1  
    
    obj=name(fname=kl,lname=y,search=z)
    obj.save()
    data=[]
    for i in range(0,len(title)-1):
         data.append({"title":title[i],"channel":channel[i],"views":views[i],"img_url":img_url[i],"polarity":polarity[i]})
    return render(request,"index2.html",{"data":data})
