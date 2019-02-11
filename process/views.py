from django.shortcuts import render
import psutil,os
def index(request):
    pid = os.getpid()
    py = psutil.Process(pid)
    while(True):
        memoryUse = py.memory_info()[0]/2.**20
        cpu=psutil.cpu_percent()
        net=psutil.net_io_counters()
        r_net=net.bytes_recv
        label=["Memmory Usage","CPU usage"]

        context={
        'label':label,
        'data':memoryUse,
        'cpu':cpu,
        'net_recieve': r_net/2.**25
        }
        return render(request,'index.html',context)
