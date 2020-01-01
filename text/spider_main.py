from text import spider_mi

if __name__ == "__main__":
    urls = {'https://www.xiaomiyoupin.com/goodsbycategory?firstId=446&secondId=446&title=%E6%9C%89%E5%93%81%E6%8E%A8%E8%8D%90&spmref=YouPinPC.$Home$.list.0.37938595',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=115&secondId=115&title=%E5%AE%B6%E7%94%A8%E7%94%B5%E5%99%A8&spmref=YouPinPC.$Home$.list.0.44295933',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=116&secondId=116&title=%E6%99%BA%E8%83%BD%E5%AE%B6%E5%BA%AD&spmref=YouPinPC.$Home$.list.0.75172848',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=90&secondId=90&title=%E7%94%B5%E8%A7%86%E5%BD%B1%E9%9F%B3&spmref=YouPinPC.$Home$.list.0.58481935',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=1038&secondId=1038&title=%E5%AE%B6%E5%85%B7%E5%AE%B6%E8%A3%85&spmref=YouPinPC.$Home$.list.0.97852451',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=88&secondId=88&title=%E5%B1%85%E5%AE%B6%E9%A4%90%E5%8E%A8&spmref=YouPinPC.$Home$.list.0.99727882',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=1050&secondId=1050&title=%E8%BF%90%E5%8A%A8%E6%88%B7%E5%A4%96&spmref=YouPinPC.$Home$.list.0.38581063',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=114&secondId=114&title=%E5%87%BA%E8%A1%8C%E8%BD%A6%E5%93%81&spmref=YouPinPC.$Home$.list.0.4931783',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=579&secondId=579&title=%E6%89%8B%E6%9C%BA%E7%94%B5%E8%84%91&spmref=YouPinPC.$Home$.list.0.6112559',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=89&secondId=89&title=%E6%95%B0%E7%A0%81%E5%91%A8%E8%BE%B9&spmref=YouPinPC.$Home$.list.0.62615861',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=93&secondId=93&title=%E6%9C%8D%E8%A3%85%E9%85%8D%E9%A5%B0&spmref=YouPinPC.$Home$.list.0.74905842',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=335&secondId=335&title=%E9%9E%8B%E9%9D%B4%E7%AE%B1%E5%8C%85&spmref=YouPinPC.$Home$.list.0.83670864',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=91&secondId=91&title=%E6%97%A5%E7%94%A8%E6%96%87%E5%88%9B&spmref=YouPinPC.$Home$.list.0.99982374',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=310&secondId=310&title=%E7%BE%8E%E9%A3%9F%E9%85%92%E9%A5%AE&spmref=YouPinPC.$Home$.list.0.95582644',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=341&secondId=341&title=%E7%BE%8E%E5%A6%86%E4%B8%AA%E6%8A%A4&spmref=YouPinPC.$Home$.list.0.25978333',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=389&secondId=389&title=%E5%81%A5%E5%BA%B7%E4%BF%9D%E5%81%A5&spmref=YouPinPC.$Home$.list.0.5799538',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=155&secondId=155&title=%E6%AF%8D%E5%A9%B4%E4%BA%B2%E5%AD%90&spmref=YouPinPC.$Home$.list.0.85403188',
           'https://www.xiaomiyoupin.com/goodsbycategory?firstId=1077&secondId=1077&title=%E5%AE%A0%E7%89%A9%E7%94%9F%E6%B4%BB&spmref=YouPinPC.$Home$.list.0.79466496'}

    spider_mi.spider(urls)
