import requests
url_1="https://run.mocky.io/v3/57ae8489-caa8-40ac-967f-f19609ec4349"
url_2="https://run.mocky.io/v3/a7ddb4d3-ad1d-4343-b020-8c077c2a6a61"

class Camera:
    def __init__(self) -> None:
        global url_1
        global url_2
        self.dev_info=eval(requests.get(url_1).text)
        url2=eval(requests.get(url_2).text)
        print(self.__class__.__name__)
        for idx, val in enumerate(self.dev_info):
            dev_name=val["name"]
            stat_val=None
            for stat_val in url2:
                if stat_val["name"]==dev_name:
                    break
            if stat_val != None:
                self.dev_info[idx].update(stat_val)
    def setPort(self, x: int) -> None:
        find=False
        for idx, val in enumerate(self.dev_info):
            if str(x)==val["id"]:
                find=True
                break
        if find:
            port_info=(self.dev_info[idx]["port_path"]).split("/")
            for set_idx,vl in enumerate(port_info):
                if "usb" in vl:
                    self.dev_info[idx]["port"]=port_info[set_idx+1]
        else:
            print("Can't find input ID")
    def getPort(self, x: int) -> str:
        find=False
        return_info=""
        for val in self.dev_info:
            if str(x)==val["id"]:
                find=True
                break
        if find:
            if "port" in val.keys():
                return_info=f'name:{val["id"]}\nPort:{val["port"]}'
                print(return_info)
                return return_info
            else:
                print(f'ID:{x} , Port has not been set')
        else:
            print("Can't find input ID")
    def getMinIdElement(self) -> dict:
        last=len(self.dev_info)
        return_id=0
        mini_id=0
        ck_indx=0
        if last>1:
            last-=1
            i=0
            while i<last:
                if int(self.dev_info[i]["id"])<int(self.dev_info[last]["id"]):
                    ck_indx=i
                else:
                    ck_indx=last
                if int(self.dev_info[ck_indx]["id"])<mini_id:
                    return_id=ck_indx
                    mini_id=int(self.dev_info[ck_indx]["id"])
                i+=1
                last-=1
        return self.dev_info[return_id]
    def getUpgradableDevice(self) -> list:
        return_list=[]
        for val in self.dev_info:
            if "SupportUpgrade" in val:
                if val["SupportUpgrade"]:
                    return_list.append(val["name"])
        return return_list
    def removeInvalidDevice(self) -> None:
        new_list=[]
        for val in self.dev_info:
            candidate_F=0
            if not val["cameras"][0]["candidate"]:
                candidate_F+=1
            if not val["microphones"][0]["candidate"]:
                candidate_F+=1
            if not val["speakers"][0]["candidate"]:
                candidate_F+=1
            if candidate_F<3:
                new_list.append(val)
        self.dev_info=new_list
        #print(self.dev_info)
        pass
if __name__ == '__main__':
    dev=Camera()
    dev.setPort(1)
    print("\n\n")

    dev.getPort(1)
    print("\n\n")


    dev.getPort(3)
    print("\n\n")

    mini=dev.getMinIdElement()
    print(mini)
    UpgradeDev=dev.getUpgradableDevice()
    print("\n")
    print(UpgradeDev)
    print("\n")
    dev.removeInvalidDevice()
    print(dev.dev_info)