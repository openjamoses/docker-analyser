import pandas as pd
import os
import time
from Git import Git
from image_analyzer import run_main
from parser.file_contents import FileManagement

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
def main():
    repo_target_path_root = ROOT_DIR+"/outputs/clones"
    df_topic = pd.read_csv(ROOT_DIR + '/input.csv')
    Repos = df_topic.Repos.values.tolist()

    if not os.path.exists(ROOT_DIR+'/outputs'):
        os.makedirs(ROOT_DIR+'/outputs')
    if not os.path.exists(ROOT_DIR+'/outputs/logs'):
        os.makedirs(ROOT_DIR+'/outputs/logs')
    if not os.path.exists(ROOT_DIR+'/outputs/clones'):
        os.makedirs(ROOT_DIR+'/outputs/clones')
    if not os.path.exists(ROOT_DIR+'/outputs/csv'):
        os.makedirs(ROOT_DIR+'/outputs/csv')
    for index in range(len(Repos)):
        #if not file_name[index] is np.nan:
        repo = Repos[index]
        print(index, repo)
        repository_url = "https://github.com/" + repo + ".git"
        repo_name = repo.split('/')[1]
        log_tags_path = ROOT_DIR+'/outputs/logs/tags_' + repo_name+'_'+str(index)+ '.txt'
        repo_root = ROOT_DIR+'/outputs/clones/'+repo_name
        if not os.path.exists(repo_root):
            code = Git.clone_git_repository(url=repository_url, target_path=repo_target_path_root)
        else:
            code = 0
        if code == 0:
            Git.git_fetch_tags(repo_root)
            logs = Git.git_fetch_tags_sorts(repo_root, log_tags_path)
            tag_list = []
            tag_date_list = []
            with open(log_tags_path, "w") as text_file:
                text_file.write(logs)

            for line in logs.split('\n'):
                if len(line) > 0:
                    split_line = line.strip().split(' ')
                    tag = split_line[0]
                    tag = tag.replace('refs/tags/', '')
                    date = split_line[1]+' '+split_line[2]+ ' '+split_line[3]+' ' +split_line[4]+ ' '+split_line[5]
                    #print (tag, date)
                    tag_list.append(tag)
                    tag_date_list.append(date)
            print ('  ----total tags found: ', len(tag_list))
            if len(tag_list) > 0:
                for tag_id in range((len(tag_list))):
                    tag = tag_list[tag_id]
                    print ('     ---- now analysing: ', tag_id, tag)
                    Git.git_checkout(repo_root, tag)
                    os.chdir(ROOT_DIR)
                    run_main(repo_root, repo, tag, save_image=True)
            else:
                run_main(repo_root, repo, '', save_image=True)
            # Remove the clone project after completing analysis
            FileManagement.remove_clone(repo_root)
        time.sleep(5)
            #os.rename(repo_path, repo_path2)
if __name__ == '__main__':
    main()