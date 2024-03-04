# Inception 
<p align="center"> <small> Deep Dive In :</small></p>
<div align="center"><img align="center" width="250" height="160" src="imgs/Docker-Logo.png"></div>


# 1. Introduction
### Why should I care about Docker?
- Docker is here and there’s no point hiding. In fact, if you want the best jobs working on the best tehnologies,
you need to know Docker and containers.

### What if I’m not a developer
- If you think Docker is just for developers, prepare to have your world turned upside-down.
Most applications, even the funky cloud-native microservices ones, need high-performance production-grade
infrastructure to run on. If you think traditional developers are going to take care of that, think again. To cut
a long story short, if you want to thrive in the modern cloud-first world, you need to know Docker. But don’t
stress, this book will give you all the skills you need.

### The bad old days
- Containers have revolutionized the way applications are deployed and managed. Traditionally, each application required its own server, leading to inefficiencies and wastage. VMware's virtual machines (VMs) offered a solution by allowing multiple applications to run on a single server, optimizing resource utilization. However, VMs have drawbacks, such as resource-intensive operating systems and slow boot times.

<div align="center"><img width="350" height="200" src="https://miro.medium.com/v2/resize:fit:760/0*ybm09Y6PTPirC84O.png"></div>

- Enter containers. Popularized by tech giants like Google, containers offer a lightweight alternative to VMs. Unlike VMs, containers share the host's operating system, leading to significant resource savings and improved portability. They boot quickly and are easily portable across different environments, from laptops to cloud platforms. Containers represent a more efficient and agile approach to application deployment, reducing costs and simplifying maintenance.

### Hello Containers
- Linux containers, a cornerstone of modern computing, owe their existence to extensive collaboration and contributions within the Linux community, notably from Google LLC. Key technologies like kernel namespaces, control groups, union filesystems, and Docker have fueled the exponential growth of containers.

- Despite their complexity, containers were made accessible to a broader audience with the advent of Docker. While other operating system virtualization technologies predate Docker, such as BSD Jails and Solaris Zones, this book focuses on modern containers popularized by Docker.

- Docker, Inc. simplified container usage, democratizing their adoption and making them accessible to all. We'll delve deeper into Docker's role in the next chapter.

# 2. Docker
Docker is software for creating, managing, and orchestrating containers on Linux and Windows. It's built from various tools within the Moby open-source project. Docker, Inc., the company behind it, was founded by Solomon Hykes but he's no longer with the company. Their focus is on simplifying the process of running code from your laptop in the cloud.

<div align="center"><img align="center" width="450" height="160" src="imgs/Docker_logos.png"></div>
