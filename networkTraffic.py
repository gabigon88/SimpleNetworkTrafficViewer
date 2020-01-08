import os, time
import psutil

class NetworkTraffic():
    def get_key(self, getLoopback: bool = False):
        key_info = psutil.net_io_counters(pernic=True)
        recv = {}
        sent = {}

        if (not getLoopback):
            #依據OS排除Loopback interface
            if os.name == 'nt':
                exclude = 'Loopback Pseudo-Interface 1'
            elif os.name == 'posix':
                exclude = 'lo'
            del key_info[exclude]
        
        key_info = key_info.keys()

        for key in key_info:
            recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)
            sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)

        return key_info, recv, sent

    def get_rate(self, getLoopback: bool = False):
        key_info, old_recv, old_sent = self.get_key(getLoopback)
        time.sleep(1)
        key_info, now_recv, now_sent = self.get_key(getLoopback)
        net_in = {}
        net_out = {}
        
        for key in key_info:
            net_in.setdefault(key, float('%.2f' %((now_recv.get(key) - old_recv.get(key)) / 1024)))
            net_out.setdefault(key, float('%.2f' %((now_sent.get(key) - old_sent.get(key)) / 1024)))
        
        return key_info, net_in, net_out

    def get_info_list(self, getLoopback: bool = False):
        key_info, old_recv, old_sent = self.get_key(getLoopback)
        time.sleep(1)
        key_info, now_recv, now_sent = self.get_key(getLoopback)
        infoList = []

        for key in key_info:
            infoList.append((key, float('%.2f' %((now_recv.get(key) - old_recv.get(key)) / 1024)), float('%.2f' %((now_sent.get(key) - old_sent.get(key)) / 1024))))
        
        return infoList

    def run(self):
        self.isRun = True
        while self.isRun:
            try:
                key_info, net_in, net_out = self.get_rate()
                for key in key_info:
                    print('%s\nInput:\t %-5sKB/s\nOutput:\t %-5sKB/s\n' %(key, net_in.get(key), net_out.get(key)))
            except KeyboardInterrupt:
                exit()

    def stop(self):
        self.isRun = False


if __name__ == "__main__":
    nt = NetworkTraffic()
    # nt.run()
    key_info, net_in, net_out = nt.get_rate()
    for key in key_info:
        print('%s\n%-5sKB/s\n%-5sKB/s' %(key, net_in.get(key), net_out.get(key)))