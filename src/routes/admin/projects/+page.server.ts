import type { PageServerLoad, Actions } from './$types';
import { SERVEUR_URL } from '$env/static/private'
import { writeFile } from 'fs/promises';


export const load: PageServerLoad = () => {
    return {
        projects: fetch(`${SERVEUR_URL}/api/projects/`).then(res => res.json())
    }
}