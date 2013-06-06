import json

dict = {"Audifonos+Diademas":["http://www.mipc.com.mx/index.php/audifono-perfect-choice-pc-110545-manos-libres-retractil.html","http://www.diademastelefonicas.com/productos.aspx?cat=3","http://www.plantronics.com/us/search/index.jsp?term=mx200&page=1&siteSeachSubmit=","http://www.amazon.com/Recoil-AUTOMATIC-Headphones-Chargers-Organizer/dp/B00B155YL8/ref=pd_bxgy_e_text_z#lbhuc_138205","http://www.amazon.com/gp/product/B008JBHGR2/ref=ox_sc_sfl_title_2?ie=UTF8&psc=1&smid=ATVPDKIKX0DER","https://www.headsetbuddy.com/cart.php"],"Linked lists + Shared libs":["http://idlebrains.org/tutorials/data-structures-tutorials/singly-linked-list-tutorial/","http://idlebrains.org/tutorials/data-structures-tutorials/doubly-linked-list-tutorial/","http://www.techytalk.info/c-cplusplus-library-programming-on-linux-part-three-dynamic-libraries-using-posix-api/","http://www.cprogramming.com/tutorial/shared-libraries-linux-gcc.html"],"Papers+citations":["https://code.google.com/p/bibstuff/","https://github.com/alexras/paper-pile","https://github.com/CrossRef/pdfextract","http://labs.crossref.org/citation-formatting-service/","https://github.com/CrossRef/pdfmark","http://en.wikipedia.org/wiki/COinS","http://www.docear.org/software/add-ons/docears-pdf-inspector/","https://github.com/Docear/PDF-Inspector","http://www.refbase.net/index.php/Web_Reference_Database","http://meta-extractor.sourceforge.net/","http://www.molspaces.com/cb2bib/","http://blog.jonathansick.ca/post/34717658434/ads-to-bibdesk-command-line-pdf-ingest","http://www.stat.berkeley.edu/VIGRE/Yao_Pitman.pdf","http://www.zotero.org/support/dev/client_coding/javascript_api","https://github.com/zotero/zotero/blob/master/chrome/content/zotero/recognizePDF.js","http://en.dogeno.us/2010/02/release-a-python-script-for-organizing-scientific-papers-pyrenamepdf-py/","http://nathangrigg.net/2012/09/organizing-arxiv-articles/","https://github.com/nathan11g/arxiv2bib","http://tincman.wordpress.com/2011/01/04/research-paper-management-with-emacs-org-mode-and-reftex/","http://www-public.it-sudparis.eu/~berger_o/weblog/2012/03/23/how-to-manage-and-export-bibliographic-notesrefs-in-org-mode/","http://www.mfasold.net/blog/2009/02/using-emacs-org-mode-to-draft-papers/","http://www.mail-archive.com/emacs-orgmode@gnu.org/msg04582.html","http://stackoverflow.com/questions/10864824/organizing-my-papers-in-org-mode","http://blog.nguyenvq.com/2011/07/24/research-paper-management-or-library-with-emacs/","http://tincman.wordpress.com/2011/01/04/research-paper-management-with-emacs-org-mode-and-reftex/","http://www.mfasold.net/blog/2009/02/using-emacs-org-mode-to-draft-papers/"],"PhysOrg Mar 2013":["http://phys.org/news/2013-03-ephemeral-vacuum-particles-speed-of-light-fluctuations.html#nwlt","http://phys.org/news/2013-03-phinergy-aluminum-air-battery-capable-fueling.html#nwlt","http://phys.org/news/2013-03-easy-identity-cell.html#nwlt","http://phys.org/news/2013-03-similarities-genetic-codes.html#nwlt","http://medicalxpress.com/news/2013-03-closer-human-heart.html#nwlt","http://phys.org/news/2013-03-fiber-cable-capable-light-in-vacuum-throughput.html#nwlt","http://phys.org/news/2013-03-artificial-muscle-universal-turing-machine.html#nwlt","http://phys.org/news/2013-03-enable-bulk-silicon-emit-visible.html#nwlt"],"Kurzweil Mar 2013":["http://www.kurzweilai.net/a-new-way-to-freeze-molecules-for-quantum-computing?utm_source=KurzweilAI+Weekly+Newsletter&utm_campaign=5718d90760-UA-946742-1&utm_medium=email","http://www.kurzweilai.net/biological-transistor-enables-computing-within-living-cells?utm_source=KurzweilAI+Weekly+Newsletter&utm_campaign=5718d90760-UA-946742-1&utm_medium=email","http://www.kurzweilai.net/better-than-x-rays-a-more-powerful-terahertz-imaging-system?utm_source=KurzweilAI+Weekly+Newsletter&utm_campaign=5718d90760-UA-946742-1&utm_medium=email","http://www.kurzweilai.net/new-solar-structure-cools-buildings-in-full-sunlight-replacing-air-conditioners?utm_source=KurzweilAI+Weekly+Newsletter&utm_campaign=5718d90760-UA-946742-1&utm_medium=email","http://www.kurzweilai.net/a-japanese-robot-car-that-drives-itself-on-sidewalks-and-footpaths?utm_source=KurzweilAI+Weekly+Newsletter&utm_campaign=5718d90760-UA-946742-1&utm_medium=email","http://www.kurzweilai.net/iron-man-meets-hulc-as-lockheed-enters-exoskeletons-race?utm_source=KurzweilAI+Weekly+Newsletter&utm_campaign=5718d90760-UA-946742-1&utm_medium=email","http://www.kurzweilai.net/metascreen-forms-ultra-thin-invisibility-cloak?utm_source=KurzweilAI+Weekly+Newsletter&utm_campaign=5718d90760-UA-946742-1&utm_medium=email","http://www.kurzweilai.net/using-carbon-nanotubes-as-qubits-for-quantum-computers?utm_source=KurzweilAI+Weekly+Newsletter&utm_campaign=5718d90760-UA-946742-1&utm_medium=email","http://www.kurzweilai.net/who-lives-longest?utm_source=KurzweilAI+Weekly+Newsletter&utm_campaign=5718d90760-UA-946742-1&utm_medium=email","http://www.kurzweilai.net/big-banks-vs-bitcoin-libertarianism?utm_source=KurzweilAI+Weekly+Newsletter&utm_campaign=5718d90760-UA-946742-1&utm_medium=email","http://www.kurzweilai.net/a-strange-computer-promises-great-speed?utm_source=KurzweilAI+Weekly+Newsletter&utm_campaign=5718d90760-UA-946742-1&utm_medium=email","http://www.kurzweilai.net/the-future-of-education-eliminates-the-classroom-because-the-world-is-your-class?utm_source=KurzweilAI+Weekly+Newsletter&utm_campaign=5718d90760-UA-946742-1&utm_medium=email"],"Mobile CAD":["http://www.cadalyst.com/management/a-mobile-cad-reality-check-part-2-14344","http://www.lenovo.com/products/us/desktop/ideacentre/horizon/?iPromoID=bannerHorizon&","http://store.sony.com/c/VAIO-Tap-20-Touchscreen-Computers/en/c/S_J2_SERIES_PAGE","https://www.asus.com/AllinOne_PCs/"],"LLVM":["http://www.drdobbs.com/architecture-and-design/the-design-of-llvm/240001128","http://npcontemplation.blogspot.mx/2008/06/secret-of-llvm-c-bindings.html","http://eli.thegreenplace.net/2012/11/24/life-of-an-instruction-in-llvm/","http://stackoverflow.com/questions/1838304/call-the-llvm-jit-from-c-program","http://llvm.org/docs/index.html","http://stackoverflow.com/questions/3509215/llvm-jit-and-native","http://llvm.org/docs/tutorial/LangImpl4.html","http://en.wikipedia.org/wiki/X_Macro","http://en.wikipedia.org/wiki/Template_metaprogramming","http://en.wikipedia.org/wiki/Objective-C","http://en.wikipedia.org/wiki/Low_Level_Virtual_Machine","http://en.wikipedia.org/wiki/Just-in-time_compilation","http://en.wikipedia.org/wiki/Self-modifying_code","http://en.wikipedia.org/wiki/Reflection_(computer_programming)","http://stackoverflow.com/questions/11733169/how-function-and-data-pointers-permit-ad-hoc-run-time-polymorphism-in-c"],"Artículos AJP":["http://ajp.aapt.org/resource/1/ajpias/v81/i4/p274_s1?isAuthorized=no","http://ajp.aapt.org/resource/1/ajpias/v80/i3/p211_s1?isAuthorized=no","http://ajp.aapt.org/resource/1/ajpias/v78/i12/p1425_s1?isAuthorized=no","http://ajp.aapt.org/resource/1/ajpias/v78/i12/p1297_s1?isAuthorized=no"],"inotify monitor folder":["http://askubuntu.com/questions/43846/how-to-put-a-trigger-on-a-directory","http://unix.stackexchange.com/questions/24952/script-to-monitor-folder-for-new-files","http://blog.chmouel.com/2009/07/03/update-emacsvim-tags-with-inotify/"],"org-mode":["http://stackoverflow.com/questions/12052013/beautiful-websites-using-emacss-org-mode","http://blog.everythingtastesbetterwithchilli.com/2013/02/10/org-mode-as-exocortex-introduction-to-mobile-org/","http://www.chawdhary.co.uk/2012/07/04/xdg-org-protocol.html","http://orgmode.org/manual/MobileOrg.html","http://blog.gabrielsaldana.org/quick-note-taking-with-emacs-and-org-capture/","http://members.optusnet.com.au/~charles57/GTD/org_dates/","http://www.neilsmithline.com/blog/page/2/","http://nibrahim.net.in/2011/07/17/my_org_mode_setup.html","http://members.optusnet.com.au/~charles57/GTD/gtd_workflow.html#sec-13","http://www.headhole.org/organisation/2012/08/22/org-mode-gtd-and-the-pomodoro-technique/"]}

for i in dict:
    fp = open(i,"w")
    fp.write("\"%s\":{%s}" % (i,json.dumps(dict[i])))
