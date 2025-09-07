.. AIO2025-Share-Value-Together 
.. AIO25-RESEARCH
.. Research
.. 2P1-05
.. 2P1-05-report

LoRA Diffuser : Fine-tuning a Stable Diffusion model to adapt to a custom dataset
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Hugging Face : `stable-diffusion-v1-5/stable-diffusion-v1-5 <https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5>`_

Prerequisites
~~~~~~~~~~~~~

1. Tổng quan vể dự án
~~~~~~~~~~~~~~~~~~~~~
- Tên dự án :  
- Link Github/Nguồn : 
- Mục tiêu dự án : 
- Nhóm thực hiện : 

2. Môi trường và công cụ thực hiện
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Cấu hình sử dụng :  
- Công cụ và thư viện chính : 

3. Quá trình tìm hiểu và thực hiện
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Tìm hiểu ban đầu :  
- Cài đặt và chạy thử : 
- Phân tích sâu và thử nghiệm : 

4. Kết quả đạt được
~~~~~~~~~~~~~~~~~~~
- Kết quả định lượng :  
- Kết quả định tính : 

5. Kinh nghiệm và kiến thức
~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Về kiến thức chuyên môn :  
- Về kỹ năng kỹ thuật : 
- Khó khăn lớn nhất và cách vượt qua :  
- Hướng phát triển/cải tiến trong tương lai : 

#Installation
~~~~~~~~~~~~~
Guide on how experience this project using Google Colab

#. .. admonition:: Clone GitHub repo and install environment

      1.1 Clone the project from GitHub :

      .. code-block:: bash

         !git clone https://github.com/phamkhanhquan197/LoRADiffuser.git

      1.2. Navigate to the project's folder :

      .. code-block:: bash

         cd LoRADiffuser

      1.3. Install the necessary libraries :

      .. code-block:: bash

         !pip install -r requirements.txt

#. .. admonition:: Load dataset and train the model

      2.1 Load the dataset :

      .. code-block:: bash

         !python dataset.py

      2.2. Create the training script :

      .. code-block:: bash
      
         #Create file : run.sh
         cat <<'EOF' > run.sh
         export MODEL_NAME="runwayml/stable-diffusion-v1-5"
         export INSTANCE_DIR="./data/flowers"
         export OUTPUT_DIR="./exps/output_dsn"

         # Run the LoRA-PTI Training script
         lora_pti \ 
           --pretrained_model_name_or_path=$MODEL_NAME \
           --instance_data_dir=$INSTANCE_DIR \ 
           --output_dir=$OUTPUT_DIR
         EOF

      2.3 Run the training script :

      .. code-block:: bash

         !chmod +x run.sh
         !./run.sh
         
#. .. admonition:: Injecting LoRA into a Stable Diffusion Model

      .. code-block:: bash

         !python3 main.py

#. .. admonition:: Generating Images

      4.1 Define the prompts for generation :

      .. code-block:: bash

         prompts = [
            "A beautiful flower in a fantasy garden",
            "A futuristic city at night",
            "A serene beach during sunset",
            "A robot painting a landscape",
            "A fantasy castle floating in clouds"
         ]

      4.2 Evaluate the model and compute the CLIP score :

      .. code-block:: bash

         !python3 evaluate.py

      4.3 Generate and save images :

      .. code-block:: bash

         ./eval_results

#. .. admonition:: Display the generated images

      .. code-block:: bash

         import glob
         from PIL import Image

         for img_path in glob.glob("./eval_results/*.png"):
         img = Image.open(img_path)
         display(img)

#. .. admonition:: 6 — Create Data Collator

      Notes about batching.

#. .. admonition:: 7 — Metrics

      Accuracy, loss, etc.

#. .. admonition:: 8 — Training Model

      Walkthrough of training loop.

#. .. admonition:: 9 — Inference

      Running inference after training.

#. .. admonition:: 10 — Evaluation

      Model performance testing.

#. .. admonition:: 11 — LoRA Rank

      Explain rank settings.

#References
^^^^^^^^^^^

#Diffusion Models
^^^^^^^^^^^^^^^^^

#Related Papers
^^^^^^^^^^^^^^^