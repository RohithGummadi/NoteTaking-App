from website import create_app

app=create_app()

if __name__== '__main__':
    app.run(debug=True) #any change re-run the webserver
    #only this file 
