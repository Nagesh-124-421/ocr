from fastapi import FastAPI, File, UploadFile,Form
import os
from pathlib import Path
from core_logic import isImageOrPdf,return_pdf_info,return_img_info


app = FastAPI()

@app.post("/upload-file/")
async def create_upload_file(file: UploadFile = File(...)):
    
    info_exctarcted=''

    try:
        # Save the file locally
        file_location = f"temp/{file.filename}"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        with open(file_location, "wb+") as file_object:
            file_object.write(await file.read())
            
            
            
        file_extension=isImageOrPdf(file.filename)
        
        if file_extension=='image':
            info_exctarcted=return_img_info(file_location)
        elif file_extension=='pdf' :
            info_exctarcted=return_pdf_info(file_location)       
        else:
            return 'please provide image or pdf'
        
        
        # Delete the file
        os.remove(file_location)
            
        

        # Process the file
        return info_exctarcted
    except Exception as e:
        print(e)
        return 'something went wrong'

    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)